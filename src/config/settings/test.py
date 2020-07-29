# -*- coding:utf-8 -*-
import os
from config.settings.base import *

SITE_URL = 'http://localhost'

# テストではローカルストレージを設定
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = '/tmp/'

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME_TEST']
DEBUG = os.environ['DEBUG'] == 'TRUE'
