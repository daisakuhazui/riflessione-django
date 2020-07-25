# -*- coding:utf-8 -*-
from django.db import models
import os
import storages.backends.s3boto3
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# アップロードストレージ定義(環境変数で定義)
if os.environ['UPLOAD_STORAGE'] == 'S3':
    # S3プライベート設定(有効期限は1ヶ月)
    protected_storage = storages.backends.s3boto3.S3Boto3Storage(
        acl='private',
        querystring_auth=True,
        querystring_expire=2678400)
else:
    # ローカルストレージ利用時
    protected_storage = FileSystemStorage(location=settings.MEDIA_ROOT)


class Category(models.Model):
    """Category Class"""
    name = models.CharField(max_length=50, blank=False,
                            null=False, verbose_name=u'カテゴリ')
    image = models.ImageField(upload_to='category/image/%Y%m%d', db_index=True,
                              blank=False, verbose_name=u'カテゴリイメージ',
                              null=False, storage=protected_storage)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'カテゴリ'
        verbose_name_plural = u'カテゴリ'


class Question(models.Model):
    """Question Class"""
    text = models.TextField(max_length=255, blank=False,
                            null=False, verbose_name=u'本文')
    category = models.ManyToManyField(
        Category, verbose_name=u'カテゴリ', blank=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u'質問'
        verbose_name_plural = u'質問'
