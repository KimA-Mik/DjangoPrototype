from .models import *


def GetGameItemByIdOrNone(id: int) -> GameItem:
    games = GameItem.objects.get(id=id)
    
    return games

def GetGenreByIdOrNone(id: int) -> Genre:
    genre = Genre.objects.get(id=id)
    
    return genre


def GetLatestsGamesList(count: int):
    list = GameItem.objects.order_by("release_date")[:count]
    return list

def GetGenresList():
    genres = Genre.objects.all()
    
    if len(genres) > 0:
        return genres
    return None

def GetGameItemByGenreOrNone(genre_id) -> GameItem:
    games = GameItem.objects.filter(genres__in=[genre_id])
    
    if len(games) > 0:
        return games
    return None