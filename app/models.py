from django.db import models
from django.core.validators import *

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=100,primary_key=True,validators=[MaxLengthValidator(10)])
    id = models.IntegerField()
    email = models.EmailField()
