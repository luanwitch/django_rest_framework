import django.contrib.admin 
from django.urls import path, include

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls), 
    path('api/', include('api.urls')),
]