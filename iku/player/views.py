from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from mutagen.mp3 import MP3


# Create your views here.
def home(request, id=1, playlist=1):
    songs = Song.objects.all()
    selected_song = Song.objects.get(pk=id)
    song_location = selected_song.file
    song_lenght = MP3(selected_song.file)
    sel_playlist = Playlist.objects.get(pk=playlist)
    playlists = Playlist.objects.all()
    context = {
        "songs":songs,
        "selected_song":selected_song,
        "song_location":song_location,
        "song_lenght":round(song_lenght.info.length, 1),
        "playlists":playlists[:5],
        "sel_playlist":sel_playlist
    }
    
    return render(request, "index.html", context)