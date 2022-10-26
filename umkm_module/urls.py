from django.urls import path
from umkm_module.views import show_umkm

application = "umkm_module"

urlpatterns = [
    path('', show_umkm, name="show_umkm"),
]