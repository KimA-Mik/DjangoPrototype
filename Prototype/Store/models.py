from django.db import models


class Genre(models.Model):
    id = models.Index
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)

    def __str__(self):
        return 'Genre: ' + self.name

class GameItem(models.Model):
    id = models.Index
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    release_date = models.DateField("release date")
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return 'Game: ' + self.title
