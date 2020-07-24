# -*- coding:utf-8 -*-
from django.db import models


class Category(models.Model):
    """Category Class"""
    name = models.CharField(max_length=50, blank=False,
                            null=False, verbose_name=u'カテゴリ')

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
