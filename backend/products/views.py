from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from categories.models import Category
from .models import Product
from . import serializers
from accounts.views import MyPagination


class ListProducts(ListAPIView):
    queryset = Product.objects.filter(hide=False)
    serializer_class = serializers.ProductsSerializerm1
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'body', 'manufacturer_company', 'categories__name']


class ListProductsByCategory(ListAPIView):
    serializer_class = serializers.ProductsSerializerm1
    def get_queryset(self):
        slug = self.kwargs['slug']
        category_obj = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(categories=category_obj)
        return products


class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm2


class DetailDeleteProduct(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm1


class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm2
