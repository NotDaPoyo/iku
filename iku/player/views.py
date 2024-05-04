from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from mutagen.mp3 import MP3


# Create your views here.
def home(request, id=1, play_list=1):
    songs = Song.objects.all()
    selected_song = Song.objects.get(pk=id)
    song_location = selected_song.file
    song_lenght = MP3(selected_song.file)
    prev_song = Song.objects.filter(playlist=play_list, id__lt=id).order_by('-id').first()
    next_song = Song.objects.filter(playlist=play_list, id__gt=id).order_by('id').first()
    if prev_song == None:
        prev_song = Song.objects.filter(playlist=play_list).order_by('-id').first()
    if next_song == None:
        next_song = Song.objects.filter(playlist=play_list).order_by('id').first()

    playlists = Playlist.objects.all()
    sel_playlist = Playlist.objects.get(id=play_list)

    context = {
        "songs":songs,
        "selected_song":selected_song,
        "song_location":song_location,
        "song_lenght":round(song_lenght.info.length, 1),
        "playlists":playlists[:5],
        "sel_playlist":sel_playlist,
        "prev_song":prev_song,
        "next_song":next_song,
    }
    
    return render(request, "index.html", context)

def redirectHome(request):
    return redirect('/home')