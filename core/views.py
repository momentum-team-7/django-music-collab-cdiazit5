from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist

# Create your views here.
def album_posts(request):
    albums = Album.objects.all()
    return render(request, 'music_temps/album_posts.html', {'albums': albums})

def artist_posts(request):
    artists = Artist.objects.all()
    return render(request, 'music_temps/artist_posts.html', {'artists': artists})

# getting album details
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'music_temps/details_album.html', {'album':album})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'music_temps/details_artist.html', {'artist':artist})

def index(request):
    return render(request, 'music_temps/index.html')