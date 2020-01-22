#!/bin/bash

# 启动horizon
cd ~/code/mydjango
source .venv/bin/activate

echo "启动服务的端口号:"
while read po;
    do python3 mysite/manage.py runserver ${po};
    done