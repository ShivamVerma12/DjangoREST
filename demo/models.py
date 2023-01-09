
from django.db import models


# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    age = models.IntegerField()



