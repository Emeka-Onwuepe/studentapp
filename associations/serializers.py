from rest_framework import serializers
from .models import Type_of_Association, Association


class Type_of_Association_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Type_of_Association
        fields= "__all__"

class Association_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Association
        fields= "__all__"