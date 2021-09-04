from django.db import models
from events.models import Grouped_Events,Single_Event

# Create your models here.

class Institution(models.Model):
    name = models.CharField("name", max_length = 150)
    location = models.CharField("name",max_length = 150)
    grouped_events = models.ManyToManyField(Grouped_Events,related_name="institution_events")
    single_events = models.ManyToManyField(Single_Event, related_name="institution_single_events")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'


    