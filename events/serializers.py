from rest_framework import serializers
from .models import Single_Event, Grouped_Events


class Single_Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Single_Event
        fields= "__all__"

class Grouped_Events_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Grouped_Events
        fields= "__all__"