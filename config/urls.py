from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# View simples para a raiz "/"
def home(request):
    return HttpResponse("Django está rodando no Docker!")

urlpatterns = [
    path('admin/', admin.site.urls),   # rota para o admin
    path('api/', include('api.urls')), # rota para a API
    path('', home),                    # rota raiz para teste
]
