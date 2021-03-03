from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist
from .forms import AlbumForm, ArtistForm

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

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')
        
    else:
        form = AlbumForm()

    return render(request, 'music_temps/add_album.html', {'form':form})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')

    else:
        form = ArtistForm()

    return render(request, 'music_temps/add_artist.html', {'form':form})

def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')

    else:
        form = ArtistForm(instance=artist)
    return render(request, 'music_temps/edit_artist.html', {'form':form, 'artist':artist})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home')

    else:
        form = AlbumForm(instance=album)
    return render(request, 'music_temps/edit_album.html', {'form':form, 'album':album})

def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/home')