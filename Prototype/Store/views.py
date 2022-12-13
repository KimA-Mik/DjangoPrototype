from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import GameItem
from .services import *

def index(request):
    latestsGames = GetLatestsGamesList(count = 5)
    template = loader.get_template('StoreTemplates/index.html')
    context = {
        'latest_games_list': latestsGames
    }
    return HttpResponse(template.render(context, request))


def game(request, game_id):
    template = loader.get_template('StoreTemplates/gamePage.html')
    game = GetGameItemByIdOrNone(game_id)

    context = {
            'game': game
        }

    return HttpResponse(template.render(context, request))

def genres(request):
    genres = GetGenresList()
    if genres is None:
        template = loader.get_template("StoreTemplates/500Error.html")
        return HttpResponse(template.render())

    template = loader.get_template("StoreTemplates/genres.html")
    context = {
        'genresList': genres
    }
    return HttpResponse(template.render(context, request))

def genre(request, genre_id):
    template = loader.get_template('StoreTemplates/genericGamesList.html')
    
    genre = GetGenreByIdOrNone(genre_id)
    if genre is None:
        template = loader.get_template("StoreTemplates/500Error.html")
        return HttpResponse(template.render())

    genreName = genre.name
    gamesList = GetGameItemByGenreOrNone(genre_id)

    context = {
            'listTitle' : f"Игры жанра {genreName}",
            'gamesList': gamesList
        }

    return HttpResponse(template.render(context, request))