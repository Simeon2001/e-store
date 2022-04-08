from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import Product_serial
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# Create your views here.
@api_view()
@permission_classes([AllowAny])
def all_Product (request):
    product = Product.objects.all()
    serializer_class = Product_serial(product,many=True)
    return Response(serializer_class.data)