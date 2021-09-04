from rest_framework import serializers
from .models import Security_alert_type, Security_Alert

class Security_alert_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Security_alert_type
        fields= "__all__"

class Security_AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Security_Alert
        fields= "__all__"