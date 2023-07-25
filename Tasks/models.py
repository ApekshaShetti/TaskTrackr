from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    date = models.DateField(default=datetime.datetime.today)
    category = models.CharField(max_length=50)

