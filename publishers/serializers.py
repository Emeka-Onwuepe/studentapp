from rest_framework import serializers
from .models import Publisher

class Publisher_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields= "__all__"