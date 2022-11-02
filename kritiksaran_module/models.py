from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    username = models.CharField(max_length=200)
    setuju = models.ManyToManyField(User, blank=True, related_name='setuju', default=0)

    def __str__(self):
        return self.title

    def amount(self):
        return self.all().count()

    def num_likes(self):
        return self.liked.all().count()

    def num_setuju(self):
        return self.setuju.all().count()


class Setuju(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="setujuer")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ="comment")

    def __str__(self):
        return f"{self.user}-{self.post}"


