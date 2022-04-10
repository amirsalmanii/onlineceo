from rest_framework import serializers
from .models import Product
from categories.serializers import CategoriesUpdateSerializer


class ProductsSerializerm1(serializers.ModelSerializer):
    categories = CategoriesUpdateSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductsSerializerm2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
