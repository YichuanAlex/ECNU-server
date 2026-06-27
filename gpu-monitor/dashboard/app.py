# dashboard/app.py
import dash
from dash import html, dcc, dash_table
import requests
import pandas as pd
from dash.dependencies import Input, Output, State

# 在这里配置你的服务器列表
MONITOR_NODES = [
    {"name": "lx", "url": "http://localhost:8000/metrics"},
    {"name": "shared0", "url": "http://localhost:8001/metrics"},
    {"name": "share1", "url": "http://localhost:8002/metrics"}
]

app = dash.Dash(__name__)

PAGE_STYLE = {
    "minHeight": "100vh",
    "padding": "28px 20px 42px",
    "background": "radial-gradient(circle at 15% 15%, #d2f4ff 0%, #f3fff9 38%, #fff7e8 100%)",
    "fontFamily": '"Avenir Next", "PingFang SC", "Microsoft YaHei", sans-serif'
}

CONTAINER_STYLE = {
    "maxWidth": "1180px",
    "margin": "0 auto"
}

HEADER_CARD_STYLE = {
    "background": "linear-gradient(120deg, #0f766e 0%, #1d4ed8 100%)",
    "padding": "22px 24px",
    "borderRadius": "16px",
    "boxShadow": "0 14px 35px rgba(15, 23, 42, 0.18)",
    "color": "#f8fafc",
    "marginBottom": "18px"
}

PANEL_STYLE = {
    "background": "rgba(255, 255, 255, 0.88)",
    "backdropFilter": "blur(6px)",
    "border": "1px solid rgba(15, 23, 42, 0.08)",
    "borderRadius": "14px",
    "padding": "14px",
    "boxShadow": "0 10px 28px rgba(15, 23, 42, 0.08)"
}

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1("实验室 GPU 实时状态监控", style={"margin": "0", "fontSize": "34px", "fontWeight": "800"}),
            html.Div("5 秒自动刷新 • 点击 GPU 行查看具体进程明细", style={"marginTop": "8px", "fontSize": "14px", "opacity": 0.92})
        ], style=HEADER_CARD_STYLE),
        html.Div([
            dcc.Interval(id='interval-component', interval=5*1000, n_intervals=0), # 5秒刷新一次
            dash_table.DataTable(
                id='gpu-table',
                data=[],
                columns=[],
                style_table={"overflowX": "auto", "borderRadius": "10px"},
                style_cell={
                    "textAlign": "center",
                    "padding": "11px 10px",
                    "border": "none",
                    "fontSize": "14px",
                    "color": "#0f172a"
                },
                style_header={
                    "backgroundColor": "#0f172a",
                    "color": "#f8fafc",
                    "fontWeight": "700",
                    "letterSpacing": "0.3px",
                    "border": "none"
                },
                style_data={
                    "backgroundColor": "rgba(255, 255, 255, 0.92)",
                    "borderBottom": "1px solid #e2e8f0"
                },
                style_data_conditional=[
                    {"if": {"row_index": "odd"}, "backgroundColor": "#f8fafc"},
                    {"if": {"state": "active"}, "backgroundColor": "#e0f2fe", "border": "1px solid #7dd3fc"},
                    {"if": {"column_id": "util"}, "fontWeight": "700"},
                    {"if": {"column_id": "process_count"}, "fontWeight": "700", "color": "#0f766e"},
                ]
            ),
            html.Div("点击上表任意一行可查看该 GPU 的进程详情", style={"marginTop": "12px", "color": "#334155", "fontWeight": "600"})
        ], style=PANEL_STYLE),
        html.Div(id='gpu-detail-container', style={"marginTop": "16px"})
    ], style=CONTAINER_STYLE)
], style=PAGE_STYLE)

@app.callback(
    Output('gpu-table', 'data'),
    Output('gpu-table', 'columns'),
    Input('interval-component', 'n_intervals')
)
def update_metrics(n):
    all_data = []
    for node in MONITOR_NODES:
        try:
            res = requests.get(node['url'], timeout=1).json()
            for gpu in res:
                gpu['node'] = node['name']
                all_data.append(gpu)
        except Exception:
            all_data.append({
                "node": node['name'],
                "id": "N/A",
                "name": "Offline",
                "mem_used": "N/A",
                "mem_total": "N/A",
                "util": "N/A",
                "users": "N/A",
                "process_count": 0,
                "processes": []
            })

    if not all_data:
        return [], []

    visible_rows = []
    for item in all_data:
        visible_rows.append({
            "node": item.get("node", "N/A"),
            "id": item.get("id", "N/A"),
            "name": item.get("name", "N/A"),
            "mem_used": item.get("mem_used", "N/A"),
            "mem_total": item.get("mem_total", "N/A"),
            "util": item.get("util", "N/A"),
            "users": item.get("users", "N/A"),
            "process_count": item.get("process_count", 0),
            "processes": item.get("processes", [])
        })

    df = pd.DataFrame(visible_rows)
    columns = [
        {"name": "node", "id": "node"},
        {"name": "id", "id": "id"},
        {"name": "name", "id": "name"},
        {"name": "mem_used", "id": "mem_used"},
        {"name": "mem_total", "id": "mem_total"},
        {"name": "util", "id": "util"},
        {"name": "users", "id": "users"},
        {"name": "process_count", "id": "process_count"},
    ]
    return df.to_dict('records'), columns


@app.callback(
    Output('gpu-detail-container', 'children'),
    Input('gpu-table', 'active_cell'),
    State('gpu-table', 'data')
)
def show_process_details(active_cell, rows):
    if not rows:
        return html.Div("暂无数据", style=PANEL_STYLE)

    if not active_cell:
        return html.Div("请选择一行查看该 GPU 的进程详情", style=PANEL_STYLE)

    row_idx = active_cell.get('row')
    if row_idx is None or row_idx >= len(rows):
        return html.Div("请选择一行查看该 GPU 的进程详情", style=PANEL_STYLE)

    row = rows[row_idx]
    processes = row.get("processes", [])

    title = html.H3(
        f"节点 {row.get('node', 'N/A')} - GPU {row.get('id', 'N/A')} 进程详情",
        style={"marginBottom": "10px", "color": "#0f172a"}
    )

    if not processes:
        return html.Div([title, html.P("当前 GPU 无活跃进程。", style={"margin": "0", "color": "#334155"})], style=PANEL_STYLE)

    process_df = pd.DataFrame(processes)
    for col in ["pid", "user", "name", "gpu_mem", "cmd"]:
        if col not in process_df.columns:
            process_df[col] = "N/A"

    process_df = process_df[["pid", "user", "name", "gpu_mem", "cmd"]]
    return html.Div([
        title,
        dash_table.DataTable(
            data=process_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in process_df.columns],
            style_table={"overflowX": "auto"},
            style_cell={'textAlign': 'left', 'padding': '9px 10px', 'maxWidth': '380px', 'whiteSpace': 'normal', 'border': 'none'},
            style_header={'backgroundColor': '#1e293b', 'color': '#f8fafc', 'fontWeight': '700', 'border': 'none'},
            style_data={'backgroundColor': 'rgba(255, 255, 255, 0.92)', 'borderBottom': '1px solid #e2e8f0'},
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#f8fafc"},
                {"if": {"column_id": "gpu_mem"}, "fontWeight": "700", "color": "#0f766e"},
                {"if": {"column_id": "pid"}, "fontFamily": '"SFMono-Regular", Menlo, Consolas, monospace'},
            ]
        )
    ], style=PANEL_STYLE)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)
