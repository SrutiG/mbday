from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class Picture(models.Model):
    picture = models.ImageField(upload_to='./static/pictures/images')
    time = models.DateTimeField(default = timezone.now())
    location = models.CharField(max_length=50)

class picture_tag(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    tag = models.CharField(max_length=20)

class picture_people(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    person = models.CharField(max_length=20)