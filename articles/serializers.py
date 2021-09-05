from rest_framework import serializers
from .models import  Article, Sub_Section


class Article_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields= "__all__"

class Sub_Section_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sub_Section
        fields= "__all__"