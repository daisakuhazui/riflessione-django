#!/bin/bash

cd /app

python src/manage.py migrate

echo "db:5432:riflessione:riflessione:riflessione" > ~/.pgpass
chmod 600 ~/.pgpass
