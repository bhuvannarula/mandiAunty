from django.db import models

# Create your models here.

class Event(models.Model):
    date = models.DateTimeField('Scheduled Date')
    duration = models.DateTimeField('Duration')
    startTime = models.DateTimeField('Time')
    name = models.CharField(max_length=200)
    descript = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    image = models.ImageField()