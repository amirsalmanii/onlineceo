from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView
)
from .models import Project
from .serializers import ProjectsSerializerm1


class ListCreateProjects(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializerm1


class DetailUpdateDeleteProjects(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializerm1
