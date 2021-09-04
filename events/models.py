from django.db import models

# Create your models here.

class Event_proto(models.Model):
    name = models.CharField("name",max_length = 150)
    venue = models.CharField("venue",max_length = 150)
    organiser_phone_number = models.CharField("organiser_phone_number",max_length = 150,blank=True,null=True)
    starting_time = models.TimeField("startin_time", auto_now=False, auto_now_add=False)
    closing_time = models.TimeField("closing_time", auto_now=False, auto_now_add=False)
    date= models.DateTimeField("date", auto_now_add=False, auto_now=False)
    fee = models.FloatField("fee", default=0.00, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Event_proto'
        verbose_name_plural = 'Event_protos'

class Event(models.Model):
    name = models.CharField("name",max_length = 150)
    description = models.CharField("description", max_length = 255, null=True, blank=True)
    event_list = models.ManyToManyField(Event_proto,related_name="event_lists")

    def __str__(self):
        self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
