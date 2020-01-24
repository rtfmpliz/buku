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
    hal = models.IntegerField(default=0)
    berat = models.IntegerField(default=0)
    harganormal = models.DecimalField(decimal_places=1,max_digits=1,default=0)
    diskon = models.DecimalField(decimal_places=1,max_digits=1,default=0)
    photo1 = models.CharField(max_length=200, default=0)
    photo2 = models.CharField(max_length=200, default=0)


    def __str__(self):
        return self.judul