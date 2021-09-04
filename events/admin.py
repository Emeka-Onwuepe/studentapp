from django.contrib import admin
from .models import Event_proto, Event

# Register your models here.

admin.site.register(Event_proto)
admin.site.register(Event)
