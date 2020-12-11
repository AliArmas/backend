from .models import Product
from .serializers import ProductSerializer

from rest_framework import viewsets, views, filters, generics
from django.shortcuts import render

# Create your views here.

class ProductView(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name','category']
    ordering_fields = ['id', 'category']
