from rest_framework import serializers
from .models import Department


class Department_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields= "__all__"