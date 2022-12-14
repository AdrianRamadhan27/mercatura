from re import search
from django.urls import path
from umkm_module.views import *

app_name = "umkm_module"

urlpatterns = [
    path('', show_umkm, name="show_umkm"),
    path('json/', show_json, name="show_json"),
    path('detail/<id>', detail_umkm,  name="detail_umkm"),
    path('detail_json/<id>', detail_umkm_json,  name="detail_umkm_json"),
    path('add_umkm/', tambah_umkm, name="tambah_umkm"),
    path('search_umkm/', search_umkm, name="search_umkm"),
    path('update_umkm/<id>', update_umkm, name="update_umkm"),
    path('add_umkm_json/', tambah_umkm_json, name="tambah_umkm_json"),
    path('search_umkm_json/', search_umkm_json, name="search_umkm_json"),
    path('update_umkm_json/<id>', update_umkm_json, name="update_umkm_json"),
]