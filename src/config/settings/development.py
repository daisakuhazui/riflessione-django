# -*- coding:utf-8 -*-
import os
from config.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True

SITE_URL = 'http://0.0.0.0:8000'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
