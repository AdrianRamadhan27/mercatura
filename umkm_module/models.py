from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UMKM(models.Model):
    nama_usaha = models.CharField(max_length=25)
    bidang_usaha = models.CharField(max_length=25)
    deskripsi_usaha = models.TextField()
    email_usaha = models.EmailField()
    lokasi_usaha = models.CharField(max_length=50)
    website_usaha = models.URLField(default="https://www.google.com/")
    logo_usaha = models.URLField(default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png")
    pemilik_usaha = models.ForeignKey(User, on_delete=models.CASCADE, default=1)