from django.test import TestCase
from django.urls import reverse, resolve
from artikel.views import *

class TestUrl(TestCase):
  def test_show_artikel_url(self):
    url = reverse("artikel:show_artikel")
    self.assertEqual(resolve(url).func, show_artikel)

  def test_show_artikel_user_url(self):
    url = reverse("artikel:show_artikel_user")
    self.assertEqual(resolve(url).func, show_artikel_user)

  def test_show_artikel_json_filter_url(self):
    url = reverse("artikel:show_artikel_user_json")
    self.assertEqual(resolve(url).func, show_artikel_json_filter)

  def test_create_artikel_url(self):
    url = reverse("artikel:create_artikel")
    self.assertEqual(resolve(url).func, create_artikel)

  def test_update_artikel_url(self):
    url = reverse("artikel:update_artikel", kwargs={"id": 1})
    self.assertEqual(resolve(url).func, update_artikel)

  def test_delete_artikel_url(self):
    url = reverse("artikel:delete_artikel", kwargs={"id": 1})
    self.assertEqual(resolve(url).func, delete_artikel)

  def test_show_artikel_json_url(self):
    url = reverse("artikel:show_artikel_json")
    self.assertEqual(resolve(url).func, show_artikel_json)
  
  def test_show_artikel_json_by_id_url(self):
    url = reverse("artikel:show_artikel_json_by_id", kwargs={"id": 1})
    self.assertEqual(resolve(url).func, show_artikel_json_by_id)