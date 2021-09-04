from rest_framework import serializers
from .models import Event_proto, Event


class Event_protoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event_proto
        fields= "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields= "__all__"