from rest_framework import serializers
from .models import Set, Level


class Level_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields= "__all__"

class Set_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields= "__all__"