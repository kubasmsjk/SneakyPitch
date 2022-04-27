from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.
def teamsView(request):
    menu = Team.objects.all()
    dane = { 'menu' : menu }
    return render(request, 'teams.html', dane)

def mainView(request):
    return render(request, 'main.html')

def tablesView(request):
    menu = Team.objects.all()
    dane = {'menu' : menu }
    return render(request, 'tables.html', dane)
