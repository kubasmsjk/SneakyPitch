from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import operator

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
    player_objects = Player.objects.all()
    dane_team = { 'team_objects' : team_objects,
                  'player_objects': player_objects }

    return render(request, 'teams.html', dane_team)

def shootersRankView(request):
    player_rank = Player.objects.all().order_by('-number_of_goals')[:10]
    context = {
        'player_rank': player_rank
    }
    return render(request, 'shootersRank.html',context)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration succesful.")
            return redirect("main")
        messages.error(request,"Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request,"You have successfully logged out.")
    return redirect("main")