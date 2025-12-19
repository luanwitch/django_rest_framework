from django.urls import path, include

urlpatterns = [
    path("products/", include("product.urls")),
    path("categories/", include("category.urls")),
    path("orders/", include("order.urls")),
]
