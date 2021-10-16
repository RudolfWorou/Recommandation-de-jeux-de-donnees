from django.db import models
from datetime import datetime
from django.forms import widgets

# Create your models here.


class Request(models.Model):
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    #start_date=models.DateField(widget=DateInput)
    #end_date=models.DateField(widget=DateInput)
    query = models.CharField(max_length = 20000)
    