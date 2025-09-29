from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer
from django.http import HttpResponse
from api.views import home


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

def home(request):
    return HttpResponse("Página inicial de tarefas 🚀")
