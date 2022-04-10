from rest_framework import serializers
from . import models


class ThreeDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ThreeD
        exclude = ('product', 'created_at')
