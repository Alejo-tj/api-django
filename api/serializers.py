
        
        
from rest_framework import serializers
from .models import Producto  # Aquí debe ser con P mayúscula

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
       