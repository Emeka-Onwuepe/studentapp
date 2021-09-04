from django.db import models
from users.models import User
from departments.models import Department

# Create your models here.

class Publisher(models.Model):
    account = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="account")
    first_name =models.CharField(verbose_name='first name', max_length=255)
    last_name =models.CharField(verbose_name='last name', max_length=255)
    description = models.TextField("description", max_length=150, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="publisher_department")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        managed = True
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'

