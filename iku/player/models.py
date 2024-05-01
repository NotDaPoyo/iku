from django.db import models

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=50)
    likes = models.DecimalField(decimal_places=0, max_digits=99)

    def __str__(self):
        return self.name


class Song(models.Model):
    author = models.ForeignKey(Musician, on_delete=models.CASCADE)
    file = models.FileField(upload_to="songs")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    lenght = models.DecimalField(decimal_places=2, max_digits=200)

    def __str__(self):
        return self.name