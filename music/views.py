from django.shortcuts import render
from .models import Album
from django.http import Http404

def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album' : all_album,
    }
    return render(request, 'music/index.html', context )

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")
    return render(request, 'music/detail.html', {'album': album})