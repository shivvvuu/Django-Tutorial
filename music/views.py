from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader
# Create your views here.

def index(request):
    all_album = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_album' : all_album,
    }
    return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2>Detais for album id:" + str(album_id)+"</h2>")