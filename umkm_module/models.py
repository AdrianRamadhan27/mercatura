from django.db import models

# Create your models here.
class UMKM(models.Model):
    nama_usaha = models.CharField(max_length=25)
    bidang_usaha = models.TextField()
    deskripsi_usaha = models.TextField()
    kontak_usaha = models.EmailField()
    lokasi_usaha = models.CharField(max_length=50)
    website_usaha = models.URLField(default="https://www.google.com/")