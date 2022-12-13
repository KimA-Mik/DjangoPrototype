from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/<int:game_id>/', views.game, name='game'),
    path('genres/', views.genres, name='genres'),
    path('genres/<int:genre_id>/', views.genre, name='genre')
]
