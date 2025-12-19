# config/urls.py
from rest_framework.routers import DefaultRouter
from category.views import CategoryViewSet
from product.views import ProductViewSet
# from order.views import OrderViewSet 

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
# router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
]