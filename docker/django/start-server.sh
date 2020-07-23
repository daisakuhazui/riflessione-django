#!/bin/bash

source ~/.bashrc
cd /app

# log/application.log がなかったらdjangoが起動しないので、
# ファイル確認して、なければ作成
if [ ! -f log/application.log ]; then
  echo "No application.log found. Creating application.log."
  touch log/application.log
fi

python src/manage.py runserver 0.0.0.0:8000
