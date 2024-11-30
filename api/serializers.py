from rest_framework import serializers
from .models import delocation

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = delocation
        fields = ('pk','longitude', 'latitude', 'images', 'is_accident', 'is_fire')