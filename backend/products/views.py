from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from categories.models import Category
from .models import Product
from . import serializers


class ListProducts(ListAPIView):
    queryset = Product.objects.filter(hide=False)
    serializer_class = serializers.ProductsSerializerm1


class ListProductsByCategory(APIView):
    def get(self, request, slug):
        category_obj = get_object_or_404(Category, slug=slug)
        queryset = Product.objects.filter(categories=category_obj)
        serializer = serializers.ProductsSerializerm1(queryset, many=True)
        return Response(serializer.data, status=200)


class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm2


class DetailDeleteProduct(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm1


class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm2
