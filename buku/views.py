from django.shortcuts import render, get_object_or_404

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
    buku = get_object_or_404(Buku, pk=buku_id)
    return render(request, 'buku/detail.html', {'buku': buku})