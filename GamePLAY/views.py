from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
# Create your views here.
def index(request):
    menu = Team.objects.all()
    dane = { 'menu' : menu }
    return render(request, 'szablon.html', dane)

def indexx(request):
    return render(request, 'index.html')

