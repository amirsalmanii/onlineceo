from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from . import serializers
from rest_framework.authtoken.models import Token


class UserListAndCreateView(ListCreateAPIView):
    """
    request get ==> users list
    request post ==> user create
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetailAndUpdateANdDelete(RetrieveUpdateDestroyAPIView):
    """
    request get ==> user detail
    request put ==> user update
    request delete ==> user delete
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
