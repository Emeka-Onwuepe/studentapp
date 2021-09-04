from django.contrib import admin
from .models import Single_Event, Grouped_Events

# Register your models here.

admin.site.register(Single_Event)
admin.site.register(Grouped_Events)
