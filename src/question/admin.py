# -*- coding:utf-8 -*-
from django.contrib import admin
from question.models import Question, Category


class CategoryAdmin(admin.ModelAdmin):
    """Category Admin Class"""
    filter_horizontal = ['question']

    def get_categories(self, obj):
        # get all categories
        return "\n".join([c.name for c in obj.category.all().order_by('name')])
    get_categories.short_description = u'カテゴリ'


class QuestionAdmin(admin.ModelAdmin):
    """Question Admin Class"""
    list_display = ['text', 'get_category']
    search_fields = ['text', 'get_category']

    def get_category(self, obj):
        return ','.join([c.name for c in obj.category.all()])


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
