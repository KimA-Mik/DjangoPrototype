from django.contrib import admin
from .models import GameItem, Genre

# Register your models here.

admin.site.register(GameItem)
admin.site.register(Genre)