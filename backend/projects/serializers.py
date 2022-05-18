from rest_framework import serializers
from .models import Project


class ProjectsSerializerm1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'