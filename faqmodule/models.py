from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Faq(models.Model):
    user = models.CharField(max_length=25, default="tester")
    title = models.CharField(max_length = 255)
    description = models.TextField()