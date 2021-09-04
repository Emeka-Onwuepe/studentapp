from django.db import models
# from django.db.models.signals import pre_save, post_delete
# from django.dispatch import receiver
import datetime
import re
from PIL import Image
from math import floor
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from sets.models import Level
from publishers.models import Publisher
# Create your models here.



class Article(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE,related_name="level")
    title = models.CharField(max_length=255)
    title_slug = models.SlugField(default="null")
    description = models.TextField()
    keywords = models.CharField(max_length=255, default="null")
    image = models.ImageField(null=True)
    image_source = models.CharField(max_length=255, null=True, blank=True)
    image_description = models.CharField(
        max_length=255, default='image', blank=True)
    sub_heading = models.CharField(max_length=255, null=True, blank=True)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(null=True)
    publisher = models.ManyToManyField(Publisher)
    view_count = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)
    references = models.TextField(default="null", null=True, blank=True)

    def bodySnippet(self):
        body = self.body_text[:120]
        bodySnippet = re.sub(
            r"\s\w+$|(<strong>|</strong>|<em>|</em>|<b>|</b>|<i>|</i>|<u>|</u>|<a.+?>|</a>)", "", body)
        return f'{bodySnippet} ....'

    def __str__(self):
        return self.title

    class Meta:
        managed = True
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-pub_date']

    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)

    def save(self, skip_md=True, *args, **kwargs):
        if skip_md:
            self.mod_date = datetime.datetime.now()

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


class Sub_Section(models.Model):
    """Model definition for Sub_Section."""
    # TODO: Define fields here
    article = models.ForeignKey(
        Article, related_name='Sub_section', on_delete=models.CASCADE)
    sub_heading = models.CharField(max_length=255, null=True, blank=True)
    Sub_section_image = models.ImageField(null=True, blank=True)
    image_source = models.CharField(max_length=255, null=True, blank=True)
    image_description = models.CharField(
        max_length=255, default="image", blank=True)
    body_text = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Sub_Section."""
        verbose_name = 'Sub_Section'
        verbose_name_plural = 'Sub_Sections'
        ordering = ['pub_date']

    def __str__(self):
        """Unicode representation of Sub_Section."""
        return self.sub_heading

    def save(self, *args, **kwargs):
        if self.Sub_section_image:
            im = Image.open(self.Sub_section_image)
            width, height = im.size
            output = BytesIO()
            n = 0.5
            Width = floor(width * n)
            Height = floor(height * n)
            if width > 1000:
                im = im.resize((Width, Height))
                im.save(output, format='JPEG', quality=100)
                output.seek(0)
                self.Sub_section_image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.Sub_section_image.name.split('.')[
                                                              0], 'image/jpeg', sys.getsizeof(output), None)

        super().save(*args, **kwargs)  # Call the real save() method

    # def delete(self, *args, **kwargs):
    #     self.Sub_section_image.delete()
    #     super().delete(*args, **kwargs)
