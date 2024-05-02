from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guess/', views.guess, name='guess'),
    path('restart/',views.restart, name='restart'),
    path('games/', views.game_list, name='game-list'),
]
