# -*- coding:utf-8 -*-
import os
from config.settings.base import *

ALLOWED_HOSTS = ['*']
SITE_URL = 'https://daisaku-portfolio.com/'
STATIC_URL = 'https://' + os.environ['STATIC_URL'] + '/'

STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEBUG = os.environ['DEBUG'] == 'TRUE'
