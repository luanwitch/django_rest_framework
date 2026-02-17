from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # Adicione isso se não tiver
    path('api/products/', include('product.urls')),
    path('api/categories/', include('category.urls')),
    path('api/orders/', include('order.urls')),
]