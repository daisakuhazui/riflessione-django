# -*- coding:utf-8 -*-
from django.views.generic import DetailView
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from question.models import Question, Category


class CategoryDetailView(DetailView):
    """Category Detail View Class"""
    template_name = 'question/detail.html'
    model = Category
    redirect_msg = 'カテゴリが見つかりませんでした。'

    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        # Check whether the question exists
        try:
            Category.objects.get(pk=kwargs['pk'])
            return super(CategoryDetailView, self).dispatch(*args, **kwargs)
        except Category.DoesNotExist:
            messages.warning(self.request, self.redirect_msg)
            return redirect('/')

    def get_context_data(self, **kwargs):
        # Get ONE question from all questions related to the category
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('id')
        context['question'] = Question.objects.filter(
            category=kwargs['object']).order_by('?')[:10].first
        return context
