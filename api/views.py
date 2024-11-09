#from rest_framework import viewsets
#from .models import producto
#from .serializers import productoSerializer

#class ProductoViewSet(viewsets.ModelViewSet):
 #   queryset = producto.objects.all()
  #  serializer_class = productoSerializer

# Create your views here.

from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
