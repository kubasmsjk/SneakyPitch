from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def mainView(request):
    return render(request, 'main.html')


def tablesView(request):
    team_objects = Team.objects.all().order_by('-points')
    context = {
        'team_objects': team_objects
    }
    return render(request, 'tables.html', context)


def queuesView(request):
    return render(request, 'queues.html')


def teamsView(request):
    team_objects = Team.objects.all()
    player_objects = Player.objects.all()
    dane_team = {'team_objects': team_objects,
                 'player_objects': player_objects}

    return render(request, 'teams.html', dane_team)


def shootersRankView(request):
    player_rank = Player.objects.all().order_by('-number_of_goals')[:10]
    context = {
        'player_rank': player_rank
    }
    return render(request, 'shootersRank.html', context)
