from django.db import models

# Create your models here.
class sendMail(models.Model):
    nama = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    email_tujuan = models.CharField(max_length=100, null=True)
    pesan = models.CharField(max_length=100, null=True)
    lampiran = models.FileField(null=True, blank=True, upload_to="attachments/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.nama_produk}"