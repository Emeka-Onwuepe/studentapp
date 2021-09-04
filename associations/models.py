from django.db import models
from events.models import Grouped_Events

# Create your models here.

class Type_of_Association(models.Model):
    """Model definition for Type_of_Association."""

    # TODO: Define fields here
    type  = models.CharField("type", max_length = 255)
    

    class Meta:
        """Meta definition for Type_of_Association."""

        verbose_name = 'Type_of_Association'
        verbose_name_plural = 'Type_of_Associations'

    def __str__(self):
        """Unicode representation of Type_of_Association."""
        return self.type


class Association(models.Model):
    """Model definition for Association."""

    # TODO: Define fields here
    association_type = models.ForeignKey(Type_of_Association, on_delete=models.CASCADE,related_name="association_type")
    name = models.CharField("name", max_length = 256)
    location  = models.CharField("location", max_length = 256)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField("phone_number", max_length = 255)
    events  = models.ManyToManyField(Grouped_Events, related_name="events")
    class Meta:
        """Meta definition for Association."""

        verbose_name = 'Association'
        verbose_name_plural = 'Associations'

    def __str__(self):
        """Unicode representation of Association."""
        return self.name



