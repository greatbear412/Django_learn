#!/bin/bash

# 启动horizon
cd ~/code/mydjango
source .venv/bin/activate

echo "启动服务的端口号:8000，是否继续? (y/你期望的端口号)"
# python3 mysite/manage.py runserver 8000;
while read po;
    do 
        if [ ${po} == "y" ]
        then
            python3 mysite/manage.py runserver 8000;
        else
            python3 mysite/manage.py runserver ${po};
        fi
    done