from django.shortcuts import render
from .models import Album
from .models import Artist

# Create your views here.
def album_posts(request):
    albums = Album.objects.all()
    return render(request, 'music_temps/album_posts.html', {'albums': albums})

def artist_posts(request):
    artists = Artist.objects.all()
    return render(request, 'music_temps/artist_posts.html', {'artist': artists})