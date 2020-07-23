#!/bin/bash

cd src
pwd
python manage.py test --settings=config.settings -v 3
