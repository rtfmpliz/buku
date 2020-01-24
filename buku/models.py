from django.db import models


# Create your models here.
class Penerbit(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama


class Penulis(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama


class Pensyarah(models.Model):
    nama = models.CharField(max_length=200)

    def __str__(self):
        return self.nama


class Buku(models.Model):
    penerbit = models.ForeignKey(Penerbit, on_delete=models.DO_NOTHING)
    judul = models.CharField(max_length=200)
    # penulis = models.ForeignKey(Penulis, on_delete=models.DO_NOTHING)
    pensyarah = models.ForeignKey(Pensyarah, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.judul