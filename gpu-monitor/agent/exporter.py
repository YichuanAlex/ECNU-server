# agent/exporter.py
from flask import Flask, jsonify
from flask_cors import CORS
import pynvml
import psutil

app = Flask(__name__)
CORS(app)

def _safe_process_details(proc):
    pid = getattr(proc, "pid", None)
    used_gpu_memory = getattr(proc, "usedGpuMemory", None)

    details = {
        "pid": pid,
        "user": "unknown",
        "name": "unknown",
        "cmd": "unknown",
        "gpu_mem": "N/A"
    }

    if used_gpu_memory not in (None, 0, 18446744073709551615):
        details["gpu_mem"] = f"{int(used_gpu_memory) // 1024**2}MB"

    if pid is None:
        return details

    try:
        process = psutil.Process(pid)
        details["user"] = process.username()
        details["name"] = process.name()
        cmdline = " ".join(process.cmdline()).strip()
        details["cmd"] = cmdline if cmdline else process.name()
    except Exception:
        pass

    return details


def get_gpu_status():
    pynvml.nvmlInit()
    try:
        gpus = []
        for i in range(pynvml.nvmlDeviceGetCount()):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
            util = pynvml.nvmlDeviceGetUtilizationRates(handle)
            name = pynvml.nvmlDeviceGetName(handle)

            process_map = {}

            for p in pynvml.nvmlDeviceGetComputeRunningProcesses(handle):
                process_map[p.pid] = _safe_process_details(p)

            try:
                for p in pynvml.nvmlDeviceGetGraphicsRunningProcesses(handle):
                    process_map[p.pid] = _safe_process_details(p)
            except Exception:
                pass

            process_list = list(process_map.values())
            users = sorted({proc["user"] for proc in process_list if proc["user"]})

            gpus.append({
                "id": i,
                "name": name if isinstance(name, str) else name.decode('utf-8'),
                "mem_used": f"{mem.used // 1024**2}MB",
                "mem_total": f"{mem.total // 1024**2}MB",
                "util": f"{util.gpu}%",
                "users": ", ".join(users) if users else "Idle",
                "processes": process_list,
                "process_count": len(process_list)
            })
        return gpus
    finally:
        try:
            pynvml.nvmlShutdown()
        except Exception:
            pass

@app.route('/metrics')
def metrics():
    return jsonify(get_gpu_status())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
