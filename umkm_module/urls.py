from re import search
from django.urls import path
from umkm_module.views import show_umkm, show_json, detail_umkm, tambah_umkm, search_umkm

app_name = "umkm_module"

urlpatterns = [
    path('', show_umkm, name="show_umkm"),
    path('json/', show_json, name="show_json"),
    path('detail/<id>', detail_umkm,  name="detail_umkm"),
    path('add_umkm/', tambah_umkm, name="tambah_umkm"),
    path('search_umkm/', search_umkm, name="search_umkm"),
    # path("upload_image", upload_image, name="upload_image")
]