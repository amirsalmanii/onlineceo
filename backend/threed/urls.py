from django.urls import path
from . import views

urlpatterns = (
    path('threed/<int:pk>/', views.DetailUpdateThreeDView.as_view(), name='update_detail_threed'),
)