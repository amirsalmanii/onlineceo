from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserListAndCreateView.as_view(), name='user_list_or_create'),
    path('user/<int:pk>/', views.UserDetailAndUpdateANdDelete.as_view(), name='user_read_update_delete'),
]