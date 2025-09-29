from django.contrib import admin
from django.urls import path, include
from api.views import home
from django.conf import settings  # <- adicione isto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
    path('', home),
]

# Apenas ativa a Debug Toolbar em DEBUG=True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
