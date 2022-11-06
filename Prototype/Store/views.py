from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import GameItem

def index(request):
    latest_games_list = GameItem.objects.order_by("release_date")[:5]
    template = loader.get_template('StoreTemplates/index.html')
    context = {
        'latest_games_list' : latest_games_list
    }
    return HttpResponse(template.render(context, request))

def game(request, game_id):
    template = loader.get_template('StoreTemplates/gamePage.html')
    game = GameItem.objects.filter(id=game_id)[0]
    context = {
        'game': game
    }
    return HttpResponse(template.render(context, request))