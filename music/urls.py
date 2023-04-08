from django.urls import path, re_path
from . import views

app_name = 'music'  # It's the name of the app diff app have diff name and for example if two or move have same url ass detail so how django will know which detail page to open name: detail have same in other apps too

urlpatterns = [
    # /music/
    path('', views.index, name='index'),
    
    # /music/<album_id>/ adding re_path for regular expression
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    
    # /music/<album_id>/favorite/
    re_path(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
