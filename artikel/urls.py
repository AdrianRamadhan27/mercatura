from django.urls import path
from artikel.views import *

app_name = 'artikel'

urlpatterns = [
  path('', show_artikel, name="show_artikel"),
  path('artikelku/', show_artikel_user, name="show_artikel_user"),
  path('json/filter/', show_artikel_json_filter, name="show_artikel_user_json"),
  path('create/', create_artikel, name="create_artikel"),
  path('edit/<int:id>/', update_artikel, name="update_artikel"),
  path('delete/<int:id>/', delete_artikel, name="delete_artikel"),
  path('create_json/', create_artikel_json, name="create_artikel_json"),
  path('edit_json/<int:id>/', update_artikel_json, name="update_artikel_json"),
  path('delete_json/<int:id>/', delete_artikel_json, name="delete_artikel_json"),
  path('json/', show_artikel_json, name="show_artikel_json"),
  path('json/<int:id>', show_artikel_json_by_id, name="show_artikel_json_by_id"),
]