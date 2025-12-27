from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet
from order.views import OrderViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet

router = DefaultRouter()
router.register(r'', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

