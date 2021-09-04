from rest_framework import serializers
from .models import Set, Level


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields= "__all__"

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Level
        fields= "__all__"