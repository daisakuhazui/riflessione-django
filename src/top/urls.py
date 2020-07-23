from django.urls import path
from top.views import Index

urlpatterns = [
    path('', Index.as_view(), name="top"),
]
