from rest_framework import serializers
from .models import Institution


class Institution_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Institution
        fields= "__all__"