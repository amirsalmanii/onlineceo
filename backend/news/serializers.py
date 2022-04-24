from rest_framework import serializers
from .models import News
from accounts.serializers import UserSerializer


class NewsSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = News
        fields = '__all__'


class NewsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'