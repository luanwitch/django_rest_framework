from django.urls import path, include
from rest_framework import routers
from api.viewsets import CategoryViewSet, ProductViewSet, OrderViewSet # type: ignore

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]