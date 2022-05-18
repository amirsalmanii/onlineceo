from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ListCreateProjects.as_view(), name='create_list_projects'),
    path('project/<int:pk>/', views.DetailUpdateDeleteProjects.as_view(), name='detail_delete_update_projects'),
]