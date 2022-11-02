from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=2000)
  date = models.DateField()
  image_url = models.URLField()