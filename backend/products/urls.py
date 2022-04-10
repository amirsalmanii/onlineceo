from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ListProducts.as_view(), name='products_list'),
    path('products/create/', views.CreateProduct.as_view(), name='products_create'),
    path('products/rd/<int:pk>/', views.DetailDeleteProduct.as_view(), name='products_read_delete'),
    path('products/u/<int:pk>/', views.UpdateProduct.as_view(), name='products_update'),
]