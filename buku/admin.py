from django.contrib import admin

# Register your models here.
from  .models import Penerbit, Buku, Pensyarah, Penulis

admin.site.register(Buku)
admin.site.register(Penerbit)
admin.site.register(Pensyarah)
admin.site.register(Penulis)