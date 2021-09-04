from django.db import models
from PIL import Image
from math import floor
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from users.models import User


# Create your models here.

class Security_alert_type(models.Model):
    name  = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Security_alert_type'
        verbose_name_plural = 'Security_alert_types'

class Security_Alert(models.Model):
    type = models.ForeignKey(Security_alert_type, on_delete=models.CASCADE, related_name="type")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    location  = models.CharField("location", max_length = 255)
    created = models.DateTimeField("created", auto_now_add=True)
    edited = models.DateTimeField("edited",auto_now=True)
    description  = models.CharField("description", max_length = 255)
    confirmation = models.FloatField("confirmation",default=0.00)
    image = models.ImageField(null=True)


    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):

        if self.image:
            im = Image.open(self.image)
            width, height = im.size
            output = BytesIO()
            n = 0.5
            Width = floor(width * n)
            Height = floor(height * n)
            if width > 1000:
                im = im.resize((Width, Height))
                im.save(output, format='JPEG', quality=100)
                output.seek(0)
                self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split(
                    '.')[0], 'image/jpeg', sys.getsizeof(output), None)

        super().save(*args, **kwargs)  # Call the real save() method

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Security_Alert'
        verbose_name_plural = 'Security_Alerts'
