from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Song(models.Model):
    author = models.ForeignKey(Musician, on_delete=models.CASCADE)
    song_file = models.FileField()
    song_name = models.CharField(max_length=100)
    song_description = models.CharField(max_length=1000)
    song_lenght = models.DecimalField(decimal_places=2, max_digits=200)