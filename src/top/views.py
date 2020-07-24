# -*- coding:utf-8 -*-
from django.views.generic import View
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from question.models import Category


class Index(View):
    """ Top Page """
    http_method_names = ["get"]
    template = "top/index.html"

    # Disable cache decorator
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Get categories
        categories = Category.objects.all().order_by('id')
        context = {'categories': categories}
        return TemplateResponse(request, self.template, context)
