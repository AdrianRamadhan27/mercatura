from http import client
from django.test import TestCase, Client
from django.urls import reverse
from artikel.views import *
from django.contrib.auth.models import User

class TestView(TestCase):
  def setUp(self):
    user = User.objects.create_user(username="dummy", password="dummy")
    post = Post.objects.create(author=user, title="dummy post", description="dummy description", date =datetime.date.today(), image_url="https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg")

  # --------------- artikel:show_artikel ---------------
  def test_show_artikel_view(self):
    result = Client().get(reverse("artikel:show_artikel"))
    self.assertEqual(result.status_code, 200)
    self.assertTemplateUsed(result, "article_home.html")

  # --------------- artikel:show_artikel_user -----------
  def test_show_artikel_user_view(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.get(reverse("artikel:show_artikel_user"))
    self.assertEqual(result.status_code, 200)
    self.assertTemplateUsed(result, "history_article.html")

  def test_create_artikel_user_view_not_logged_in(self):
    client = Client()
    result = client.get(reverse("artikel:show_artikel_user"))
    self.assertEqual(result.status_code, 302)

  # --------------- artikel:show_artikel_user_json --------------
  def test_artikel_user_json_views(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.get(reverse("artikel:show_artikel_user_json"))
    self.assertEqual(result.status_code, 200)

  # --------------- artikel:create_artikel --------------
  def test_create_artikel_view(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.post(reverse("artikel:create_artikel"), {"title": "dummy", "description": "dummy", "image_url": "https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg"})
    self.assertEqual(result.status_code, 200)

    result2 = client.get(reverse("artikel:create_artikel"))
    self.assertEqual(result2.status_code, 200)
    self.assertTemplateUsed(result2, "create_article.html")

  def test_create_artikel_view_not_logged_in(self):
    client = Client()
    result = client.get(reverse("artikel:create_artikel"))
    self.assertEqual(result.status_code, 302)

  def test_create_artikel_views_bad_request(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.post(reverse("artikel:create_artikel"), {"title": "", "description": "dummy", "image_url": "https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg"})
    self.assertEqual(result.status_code, 400)

  # --------------- artikel:update_artikel --------------
  def test_update_artikel_view(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.post(reverse("artikel:update_artikel", kwargs={"id": 1}), {"title": "dummydummy", "description": "dummy", "image_url": "https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg"})
    self.assertEqual(result.status_code, 200)

  def test_update_artikel_view_not_logged_in(self):
    client = Client()
    result = client.post(reverse("artikel:update_artikel", kwargs={"id": 1}), {"title": "dummydummy", "description": "dummy", "image_url": "https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg"})
    self.assertEqual(result.status_code, 302)

  def test_update_artikel_view_not_found(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.post(reverse("artikel:update_artikel", kwargs={"id": 200}), {"title": "dummydummy", "description": "dummy", "image_url": "https://www.harianbhirawa.co.id/wp-content/uploads/2022/02/Ganti-Rugi-UMKM-Migor-e1644234750327.jpeg"})
    self.assertEqual(result.status_code, 404)

  # --------------- artikel:delete_artikel --------------
  def test_delete_artikel_view(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.get(reverse("artikel:delete_artikel", kwargs={"id": 1}))
    self.client.delete(result)
    self.assertEqual(result.status_code, 200)

  def test_delete_artikel_view_not_logged_in(self):
    client = Client()
    result = client.get(reverse("artikel:delete_artikel", kwargs={"id": 1}))
    self.assertEqual(result.status_code, 302)

  def test_delete_artikel_view_not_found(self):
    client = Client()
    client.login(username="dummy", password="dummy")
    result = client.get(reverse("artikel:delete_artikel", kwargs={"id": 100}))
    self.assertEqual(result.status_code, 404)

  # --------------- artikel:show_artikel_json --------------
  def test_show_artikel_json_views(self):
    client = Client()
    result = client.get(reverse("artikel:show_artikel_json"))
    self.assertEqual(result.status_code, 200)

  # --------------- artikel:show_artikel_json_by_id --------------
  def test_show_artikel_json_by_id_view(self):
    client = Client()
    result = client.get(reverse("artikel:show_artikel_json_by_id", kwargs={"id": 1}))
    self.assertEqual(result.status_code, 200)

  def test_show_artikel_json_by_id_view_not_found(self):
    client = Client()
    result = client.get(reverse("artikel:show_artikel_json_by_id", kwargs={"id": 9}))
    self.assertEqual(result.status_code, 404)