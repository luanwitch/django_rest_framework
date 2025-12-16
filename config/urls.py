from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore

from api.views import ProductViewSet
from category.views import CategoryViewSet
from order.views import OrderViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', lambda req: redirect('/api/')), # Redireciona a home para a API # type: ignore
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]