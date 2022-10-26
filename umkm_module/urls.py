from django.urls import path
from umkm_module.views import show_umkm, show_json, detail_umkm

app_name = "umkm_module"

urlpatterns = [
    path('', show_umkm, name="show_umkm"),
    path('json/', show_json, name="show_json"),
    path('detail/<id>', detail_umkm,  name="detail_umkm"),
]