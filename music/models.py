from django.db import models
from django.urls import reverse

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    alum_title =models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    alum_logo = models.CharField(max_length=1000)
    
    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    
    
    
    def __str__(self) :
        return self.alum_title + '-' + self.artist
    
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.song_title
    
    