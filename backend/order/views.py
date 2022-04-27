from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import filters
from .models import Order, OrderItems, RefundOrdersRequest
from . import serializers
from accounts.views import MyPagination


class ListOrdersView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializerM1
    pagination_class = MyPagination


class CreateOrdersView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializerM2


class RestriveOrdersView(APIView):
    def get(self, request, order_id):
        order = Order.objects.get(order_id=order_id)
        order_items = OrderItems.objects.filter(order_id=order_id)

        serializer_order = serializers.OrderSerializerM1(order)
        serializer_order_items = serializers.OrderItemsSerializerM1(order_items, context={'request': request}, many=True)
        return Response({'data_1':serializer_order.data, 'data_2': serializer_order_items.data}, status=200)
    
    def put(self, request, order_id):
        order = Order.objects.get(order_id=order_id)
        serializer = serializers.OrderSerializerM2(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(serializer.errors, status=400)


class RefundsOrdersRequestView(ListAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundsSerializer
    pagination_class = MyPagination


class RefundOrderRequestDetailView(RetrieveAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundsSerializer


class RefundOrderRequestUpdateView(UpdateAPIView):
    queryset = RefundOrdersRequest.objects.all()
    serializer_class = serializers.OrderRefundUpdateSerializer