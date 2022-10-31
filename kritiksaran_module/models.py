from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    username = models.CharField(max_length=200)
    liked = models.ManyToManyField(User, blank=True, related_name='likes')
    setuju = models.ManyToManyField(User, blank=True, related_name='setuju')
    date_made = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    def num_likes(self):
        return self.liked.all().count()

    def num_setuju(self):
        return self.setuju.all().count()



# LIKE_CHOICES = (
#     ('Like', 'Like'),
#     ('Unlike', 'Unlike'),
# )

# class Like(models.Model): 
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES, max_length=8)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.user}-{self.post}-{self.value}"

class Setuju(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="setujuer")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name ="comment")

    def __str__(self):
        return f"{self.user}-{self.post}"


