from django.contrib import admin  
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import OrderViewSet

from category.views import CategoryViewSet
from product.views import ProductViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)), 
]