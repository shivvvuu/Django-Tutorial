from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
# Create your views here.

def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album' : all_album,
    }
    return render(request, 'music/index.html', context )

def detail(request, album_id):
    return HttpResponse("<h2>Detais for album id:" + str(album_id)+"</h2>")