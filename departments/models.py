from django.db import models
from faculties.models import Faculty
from events.models import Grouped_Events, Single_Event

# Create your models here.

class Department(models.Model):
    name = models.CharField("name", max_length = 150)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE,related_name="faculty")
    grouped_events = models.ManyToManyField(Grouped_Events,related_name="department_events")
    single_events = models.ManyToManyField(Single_Event, related_name="department_single_events")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
