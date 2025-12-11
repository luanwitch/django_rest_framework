from rest_framework import viewsets
from api.models import Product
from .serializers import ProductSerializer 

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar, criar, atualizar e deletar produtos.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

