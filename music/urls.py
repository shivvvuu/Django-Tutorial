from django.urls import path, re_path
from . import views

app_name = 'music'  # It's the name of the app diff app have diff name and for example if two or move have same url ass detail so how django will know which detail page to open name: detail have same in other apps too

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    
    # /music/
    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    
    # /music/<album_id>/ adding re_path for regular expression
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /music/<album_id>/favorite/
    #re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    
    #/music/album/add/
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    
    #/music/album/2/
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    
    #/music/album/2/delete 
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
