from django.db import models
from lectures.models import Day

# Create your models here.


class Exam_day_and_venue(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE,related_name="examination_day")
    starting_time = models.TimeField("startin_time", auto_now=False, auto_now_add=False)
    closing_time = models.TimeField("closing_time", auto_now=False, auto_now_add=False)
    venue  = models.CharField(max_length = 150)
    

    def __str__(self):
        return str(self.day)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Exam_day_and_venue'
        verbose_name_plural = 'Exam_days_and_venues'

class Examination(models.Model):
    course_code = models.IntegerField()
    course_title  = models.CharField("course_title", max_length = 150)
    days_and_venues = models.ManyToManyField(Exam_day_and_venue,related_name="exam_day_and_venue")
    invigilators  = models.CharField("invigilators", max_length = 250, blank=True, null=True)   
    
    def __str__(self):
        return f"{self.code} : {self.title}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Examination'
        verbose_name_plural = 'Examinations'
