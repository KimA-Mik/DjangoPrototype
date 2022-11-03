from django.db import models

# Create your models here.

class GameItem(models.Model):
    id = models.Index
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    release_date = models.DateField("release date")