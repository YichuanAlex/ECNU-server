#!/bin/bash
# 杀死已经存在的旧进程（防止端口占用）
pkill -f exporter.py
# 后台运行并将日志记录到 agent.log
nohup python exporter.py > agent.log 2>&1 &
echo "Agent is running on port 8000..."