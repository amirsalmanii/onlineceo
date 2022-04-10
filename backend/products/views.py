from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView
)
from .models import Product
from . import serializers


class ListProducts(ListAPIView):
    queryset = Product.objects.filter(hide=False)
    serializer_class = serializers.ProductsSerializerm1


class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm2


class DetailDeleteProduct(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm1


class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductsSerializerm2
