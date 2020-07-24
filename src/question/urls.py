from django.urls import path
from question.views import CategoryDetailView

app_name = 'question'
urlpatterns = [
    path('category/<int:pk>/',
         CategoryDetailView.as_view(), name='category_detail'),
]
