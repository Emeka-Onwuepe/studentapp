from rest_framework import serializers
from .models import Day, Lecture_day_and_venue, Lecture,Recommended_text

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Day
        fields= "__all__"

class Lecture_day_and_venueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecture_day_and_venue
        fields= "__all__"

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields= "__all__"

class Recommended_textSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recommended_text
        fields= "__all__"