from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    songs = Song.objects.all()
    context = {
        "songs":songs,
    }
    return render(request, "index.html", context)