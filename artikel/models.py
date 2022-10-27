from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  # author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  date = models.DateField()
  image_url = models.URLField()