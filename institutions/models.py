from django.db import models
from events.models import Grouped_Events

# Create your models here.

class Institution(models.Model):
    name = models.CharField("name", max_length = 150)
    location = models.CharField("name",max_length = 150)
    events = models.ManyToManyField(Grouped_Events,related_name="institution_events")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'


    