from django.db import models

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=50)
    likes = models.DecimalField(decimal_places=0, max_digits=99)

    def __str__(self):
        return self.name


class Song(models.Model):
    author = models.ForeignKey(Musician, on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    lenght = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    list = models.ManyToManyField(Song, blank=True, default=1)

    def get_first_song(self):
        try:
            return self.song.order_by('id')[0]
        except IndexError:
            return None
    def __str__(self):
        return f"{self.name}"
    
