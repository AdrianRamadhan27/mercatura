from django.db import models

# Create your models here.
class UMKM(models.Model):
    nama_usaha = models.CharField(max_length=25)
    bidang_usaha = models.CharField(max_length=25)
    deskripsi_usaha = models.TextField()
    email_usaha = models.EmailField()
    lokasi_usaha = models.CharField(max_length=50)
    website_usaha = models.URLField(default="https://www.google.com/")
    logo_usaha = models.ImageField(upload_to='images/')