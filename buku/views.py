from django.shortcuts import render

from django.http import HttpResponse
from  django.template import loader
from .models import Buku


def index(request):
    latest_buku_list = Buku.objects.all()
    template = loader.get_template('buku/index.html')
    output = ', '.join([b.judul for b in latest_buku_list])
    return HttpResponse(output)