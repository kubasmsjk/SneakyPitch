from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.
def teams(request):
    menu = Team.objects.all()
    dane = { 'menu' : menu }
    return render(request, 'teams.html', dane)

def index(request):
    return render(request, 'index.html')

def tables(request):
    menu = Team.objects.all()
    dane = {'menu' : menu }
    return render(request, 'tables.html', dane)
