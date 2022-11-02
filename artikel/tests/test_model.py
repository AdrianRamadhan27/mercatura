import datetime
from django.test import TestCase
from artikel.models import *
from django.contrib.auth.models import User

class TestModel(TestCase):
  def setUp(self):
    user = User.objects.create_user(username="dummy", password="dummy")
    post = Post.objects.create(author=user, title="dummy post", description="dummy description", date=datetime.date.today(), image_url="https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg")

  def test_post_models(self):
    user = User.objects.get(username="dummy")
    post = Post.objects.get(pk=1)
    self.assertEqual(post.title, "dummy post")
    self.assertEqual(post.description, "dummy description")
    self.assertEqual(post.image_url, "https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg")
    self.assertEqual(post.author, user)