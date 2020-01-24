from django.shortcuts import render

from django.http import HttpResponse, Http404
from  django.template import loader
from .models import Buku


def index(request):
    latest_buku_list = Buku.objects.all()
    template = loader.get_template('buku/index.html')
    context ={
        'latest_buku_list':latest_buku_list,
    }
    # output = ', '.join([b.judul for b in latest_buku_list])
    return HttpResponse(template.render(context,request))


def detail(request, buku_id):
    try:
        buku = Buku.objects.get(pk=buku_id)
    except Buku.DoesNotExist:
        raise Http404("Buku tidak tersedia")
    return render(request, 'buku/detail.html', {'buku': buku})