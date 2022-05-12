from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .forms import CustomUserCreationForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import operator


# Create your views here.
def mainView(request):
    static_items=StaticItems.objects.all()
    dane_items = {'static_items': static_items}
    return render(request, 'main.html', dane_items)

#@login_required(login_url='login')

def tablesView(request):
    team_objects = Team.objects.all().order_by('-points')
    context = {
        'team_objects': team_objects
    }
    return render(request, 'tables.html', context)


def queuesView(request):
    queue_objects = Match.objects.all().order_by('queue_number', 'match_date')
    dane_queue = {'queue_objects': queue_objects}
    return render(request, 'queues.html', dane_queue)


def teamsView(request):
    team_objects = Team.objects.all()
    dane_team = {'team_objects': team_objects}

    return render(request, 'teams.html', dane_team)


def shootersRankView(request):
    player_rank = Player.objects.all().order_by('-number_of_goals')[:10]
    context = {
        'player_rank': player_rank
    }

    return render(request, 'shootersRank.html', context)

def registerView(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('main')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})
# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             messages.success(request,"Registration succesful.")
#             return redirect("main")
#         messages.error(request,"Unsuccessful registration. Invalid information.")
#     form = NewUserForm()
#     return render(request=request, template_name="main.html", context={"register_form":form})
#
# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {username}.")
#                 return redirect("main")
#             else:
#                 messages.error(request,"Invalid username or password.")
#         else:
#             messages.error(request,"Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form":form})
#
# def logout_request(request):
#     logout(request)
#     messages.info(request,"You have successfully logged out.")
#     return redirect("main")
