from rest_framework import serializers
from .models import Faculty

class Faculty_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Faculty
        fields= "__all__"