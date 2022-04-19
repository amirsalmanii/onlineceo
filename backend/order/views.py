from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from .models import Order, OrderItems
from . import serializers


class ListOrdersView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializerM1


class CreateOrdersView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializerM2


class RestriveOrdersView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(order_id=order_id)
        order_items = OrderItems.objects.get(order_id=order_id)

        serializer_order = serializers.OrderSerializerM1(order)
        serializer_order_items = serializers.OrderItemsSerializerM1(order_items, context={'request': request})
        return Response({'data_1':serializer_order.data, 'data_2': serializer_order_items.data}, status=200)


