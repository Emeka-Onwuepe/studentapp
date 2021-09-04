from django.db import models

# Create your models here.

class Day(models.Model):
    day = models.CharField("day", max_length = 150)
    
    def __str__(self):
        return self.day

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Day'
        verbose_name_plural = 'Days'




class Recommended_text(models.Model):
    title = models.CharField("title", max_length = 150)
    author = models.CharField("author", max_length = 150)
    publisher  = models.CharField("publisher", max_length = 150)
    volume   = models.CharField("volume", max_length = 150, blank=True, default=1)
    year_of_publication  = models.CharField("year_of_publication", max_length = 150)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Recommended_text'
        verbose_name_plural = 'Recommended_texts'

class Lecture_day_and_venue(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE,related_name="lecture_day")
    starting_time = models.TimeField("startin_time", auto_now=False, auto_now_add=False)
    closing_time = models.TimeField("closing_time", auto_now=False, auto_now_add=False)
    venue  = models.CharField(max_length = 150)
    

    def __str__(self):
        return str(self.day)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lecture_day_and_venue'
        verbose_name_plural = 'Lectures_days_and_venues'

class Lecture(models.Model):
    course_code = models.IntegerField()
    course_title  = models.CharField("course_title", max_length = 150)
    days_and_venues = models.ManyToManyField(Lecture_day_and_venue,related_name="lecture_days_and_venues")
    Lecturers_in_charge  = models.CharField("lecturers_in_charge", max_length = 250, blank=True, null=True)
    Recommended_text = models.ManyToManyField(Recommended_text,related_name="recommended_text")
    
    def __str__(self):
        return f"{self.code} : {self.title}"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lecture'
        verbose_name_plural = 'Lectures'