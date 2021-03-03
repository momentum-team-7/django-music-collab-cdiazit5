from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'cover']
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'genre',]


# '''Django documentation on forms can be found here https://docs.djangoproject.com/en/3.1/topics/forms/'''