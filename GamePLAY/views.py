from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.
def mainView(request):
    return render(request, 'main.html')

def tablesView(request):
    team_objects = Team.objects.all()
    dane = {'team_objects' : team_objects }
    return render(request, 'tables.html', dane)

def queuesView(request):
    return render(request, 'queues.html')

def teamsView(request):
    team_objects = Team.objects.all()
    dane = { 'team_objects' : team_objects }
    return render(request, 'teams.html', dane)

def shootersRankView(request):
    return render(request, 'shootersRank.html')

