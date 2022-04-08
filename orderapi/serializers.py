from rest_framework import serializers
from .models import Product

class Product_serial (serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    
    class Meta:
        model = Product
        fields = ['id','category','name','price','available','image']
