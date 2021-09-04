from rest_framework import serializers
from .models import Single_Event, Event


class Event_protoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Single_Event
        fields= "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields= "__all__"