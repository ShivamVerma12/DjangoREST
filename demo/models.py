from django.db import models
from django.http import HttpResponseBadRequest


# Create your models here.


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    age = models.IntegerField()

