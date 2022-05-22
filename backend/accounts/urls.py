from django.urls import path
from . import views

urlpatterns = [
    path('otp/verify/', views.UserVerifyOtp.as_view(), name='verify_by_otp'),
    path('otp/confirm/', views.UserConfirmOtp.as_view(), name='confirm_after_verify'),
    path('otp/email/verify/', views.UserVerifyOtpEmail.as_view(), name='verify_byd_otp'),
    path('otp/email/confirm/', views.UserConfirmOtpEmail.as_view(), name='confirm_after_verify'),
    path('user/', views.UserListAndCreateView.as_view(), name='user_list_or_create'),
    path('user/<int:pk>/', views.UserDetailAndUpdateANdDelete.as_view(), name='user_read_update_delete'),
    path('user/ad-op/', views.UserListAdminOrOprator.as_view(), name='admin_or_op users'),
    path('user/profile/', views.UserProfile.as_view(), name='user_profile'),
    path('user/register/', views.UserRegisterView.as_view(), name='user_profile'),
    path('wallet/', views.ShowUserWallet.as_view(), name='user_wallet'),
    path('user_t_d/', views.ShowUserData.as_view(), name='user_data'),
]