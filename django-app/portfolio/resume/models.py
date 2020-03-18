from django.db import models

# Create your models here.
class school(models.Model):
    name=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)
    start=models.CharField(max_length=100)
    
