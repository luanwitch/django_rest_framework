from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet): # Tem que ser ModelViewSet
    queryset = Product.objects.all()
    serializer_class = ProductSerializer