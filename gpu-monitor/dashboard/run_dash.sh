#!/bin/bash
# 杀死已经存在的旧进程
pkill -f app.py
# 后台运行并将日志记录到 dashboard.log
nohup python3 app.py > dashboard.log 2>&1 &
echo "Dashboard is running on port 8050..."