from django.db import models

class Kisah(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    workfield = models.CharField(max_length=100)
    description = models.TextField()
