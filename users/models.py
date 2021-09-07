from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,PermissionsMixin)
from institutions.models import Institution
from faculties.models import Faculty
from associations.models import Association
from departments.models import Department
from sets.models import Set
from events.models import Grouped_Events, Single_Event



# from django.db.models.constraints import CheckConstraint


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,institution=None,faculty=None,department=None,set=None, 
                    first_name='null',last_name='null', password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),first_name=first_name,last_name=last_name,
                           institution =institution,faculty=faculty,department=department,set=set)
        user.set_password(password)
        user.save(using=self._db)
        return user
  
    def create_superuser(self, email, password):
        user = self.create_user(email,password=password,first_name="SITE",last_name="CREATOR",)
        user.is_admin = True
        user.staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    first_name =models.CharField(verbose_name='first name', max_length=255)
    last_name =models.CharField(verbose_name='last name', max_length=255)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name="user_institution", blank=True, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="user_faculty", blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="user_department",blank=True, null=True)
    set = models.ForeignKey(Set, on_delete=models.CASCADE, related_name="set", blank=True, null=True)
    rating = models.FloatField("rating",default=0.00, blank=True)
    is_institution_admin = models.BooleanField(default=False)
    is_faculty_admin = models.BooleanField(default=False)
    is_department_admin = models.BooleanField(default=False)
    is_set_admin = models.BooleanField(default=False)
    associations = models.ManyToManyField(Association,related_name="user_associations",blank=True)
    association_admin = models.ManyToManyField(Association,related_name="association_admin",blank=True)
    grouped_events = models.ManyToManyField(Grouped_Events,related_name="user_grouped_events",blank=True)
    single_events = models.ManyToManyField(Single_Event,related_name="user_single_events",blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    staff=models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        if not self.is_admin and self.staff:
            if perm =="Users.add_user" or perm=="Users.change_user" or perm=="Users.delete_user":
                return False
            else:
                return True
        else:
            return True

    # remember to set appropriate permissions.
    def has_module_perms(self, app_label):
        if not self.is_admin and self.staff:
            if app_label =="knox" or app_label=="auth" :
                return False
            else:
                return True
        else:
            return True
    @property

    def is_staff(self):
        return self.staff


