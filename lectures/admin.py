from django.contrib import admin
from .models import Day, Lecture_day_and_venue, Lecture,Recommended_text

# Register your models here.

admin.site.register(Day)
admin.site.register(Lecture_day_and_venue)
admin.site.register(Lecture)
admin.site.register(Recommended_text) 