from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.ListNewsView.as_view(), name='list_news'),
    path('news/create/', views.CreateNewsView.as_view(), name='create_news'),
    path('news/rd/<int:pk>/', views.DetailDeleteView.as_view(), name='read_delete_news'),
    path('news/u/<int:pk>/', views.UpdateNewsView.as_view(), name='update_news'),
]