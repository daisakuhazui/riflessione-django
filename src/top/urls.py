from django.urls import path
from top.views import Index, Guide

urlpatterns = [
    path('', Index.as_view(), name='top'),
    path('guide/', Guide.as_view(), name='guide'),
]
