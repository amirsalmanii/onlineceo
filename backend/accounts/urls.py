from django.urls import path
from . import views

urlpatterns = [
    path('otp/verify/', views.UserVerifyOtp.as_view(), name='verify_by_otp'),
    path('otp/confirm/', views.UserConfirmOtp.as_view(), name='confirm_after_verify'),
    path('user/', views.UserListAndCreateView.as_view(), name='user_list_or_create'),
    path('user/<int:pk>/', views.UserDetailAndUpdateANdDelete.as_view(), name='user_read_update_delete'),
]