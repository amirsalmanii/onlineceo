from django.urls import path
from . import views

urlpatterns = [
    path('categories-m1/', views.ListCategories.as_view(), name='list_category'),
    path('categories-m2/', views.ListCategories2.as_view(), name='list_category2'),
    path('categories/<int:pk>/', views.DetailDeleteUpdateCategory.as_view(), name='rud_category'),
]