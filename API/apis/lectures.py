from lectures.serializers import (Day_Serializer, Lecture_day_and_venue_Serializer,
                                 Lecture_Serializer, Recommended_text_Serializer)
from lectures.models import Day, Lecture_day_and_venue, Lecture, Recommended_text
from rest_framework import permissions,generics,status
from rest_framework.response import Response