from rest_framework import serializers
from .models import Security_alert_type, Security_Alert

class Security_alert_type_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Security_alert_type
        fields= "__all__"

class Security_Alert_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Security_Alert
        fields= "__all__"