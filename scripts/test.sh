#!/bin/bash

cd src
pwd
python manage.py test --settings=config.settings.test -v 3
