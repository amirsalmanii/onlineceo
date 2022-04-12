from rest_framework import serializers
from .models import Mark
from products.serializers import ProductsSerializerm2


class MarkSerializer(serializers.ModelSerializer):
    product = ProductsSerializerm2()

    class Meta:
        model = Mark
        fields = '__all__'
