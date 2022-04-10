from rest_framework.generics import (
    RetrieveUpdateAPIView
)
from .models import ThreeD
from . import serializers


class DetailUpdateThreeDView(RetrieveUpdateAPIView):
    """
    request get ==> detail threed
    request put ==> update fields
    """
    queryset = ThreeD.objects.all()
    serializer_class = serializers.ThreeDSerializer
