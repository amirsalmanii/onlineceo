from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.ListOrdersView.as_view(), name='orders_list'),
    path('order/create/', views.CreateOrdersView.as_view(), name='orders_create'),
    path('order/<str:order_id>/', views.RestriveOrdersView.as_view(), name='orders_create'),
    path('refunds/', views.RefundsOrdersRequestView.as_view(), name='refund_list'),
    path('refunds/<int:pk>/', views.RefundOrderRequestDetailView.as_view(), name='refund_detail'),
    path('refunds/u/<int:pk>/', views.RefundOrderRequestUpdateView.as_view(), name='refund_update'),
]