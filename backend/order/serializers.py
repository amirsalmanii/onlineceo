from rest_framework import serializers
from .models import Order, OrderItems
from accounts.serializers import UserSerializer
from products.serializers import ProductsSerializerm2

class OrderSerializerM1(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializerM2(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemsSerializerM1(serializers.ModelSerializer):
    product = ProductsSerializerm2()
    class Meta:
        model = OrderItems
        fields = '__all__'