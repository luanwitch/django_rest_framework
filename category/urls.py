from django.urls import path
from .views import CategoryListCreateView  # Verifique se o nome está idêntico

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]