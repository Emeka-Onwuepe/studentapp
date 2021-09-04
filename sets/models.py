from django.db import models
from departments.models import Department
from lectures.models import Lecture
from examinations.models import Examination
from events.models import Single_Event


# Create your models here.


class Level(models.Model):
    name = models.CharField("name", max_length=156)
    department_article = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="Department")
    # description = models.TextField(default="null", blank=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

class Set(models.Model):
    year = models.CharField("year", max_length = 150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name="department")
    events = models.ManyToManyField(Single_Event,related_name="single_event")
    lectures = models.ManyToManyField(Lecture,related_name="lecture")
    exams = models.ManyToManyField(Examination,related_name="examination")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Set'
        verbose_name_plural = 'Sets'
