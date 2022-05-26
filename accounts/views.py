from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import *


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.success(request, "Invalid username or password.")
                return redirect('main')
        else:
            messages.success(request, "Invalid username or password.")
            return redirect('main')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', context={"login_form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('main')


def register_user(request):
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
            # return redirect('main')
            return render(request, 'register.html', context)

    return render(request, 'register.html', {})


@login_required(login_url='main')
def team_create(request):
    if request.method == "POST":
        form = CreateTeam(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('players_add')
    else:
        form = CreateTeam
    return render(request, 'team-create.html', {'form': form})


@login_required(login_url='main')
def players_add(request):
    if request.method == "POST":
        form1 = CreatePlayers(request.POST, prefix="form1")
        form2 = CreatePlayers(request.POST, prefix="form2")
        form3 = CreatePlayers(request.POST, prefix="form3")
        form4 = CreatePlayers(request.POST, prefix="form4")
        form5 = CreatePlayers(request.POST, prefix="form5")
        form6 = CreatePlayers(request.POST, prefix="form6")
        form7 = CreatePlayers(request.POST, prefix="form7")
        form8 = CreatePlayers(request.POST, prefix="form8")
        form9 = CreatePlayers(request.POST, prefix="form9")
        form10 = CreatePlayers(request.POST, prefix="form10")
        form11 = CreatePlayers(request.POST, prefix="form11")
        if form1.is_valid():
            player1 = Player(first_name=form1.cleaned_data['first_name'], last_name=form1.cleaned_data['last_name'],
                             player_position=form1.cleaned_data['player_position'],
                             country=form1.cleaned_data['country'], team=Team.objects.all().last())
            player1.save()
        if form2.is_valid():
            player2 = Player(first_name=form2.cleaned_data['first_name'], last_name=form2.cleaned_data['last_name'],
                             player_position=form2.cleaned_data['player_position'],
                             country=form2.cleaned_data['country'], team=Team.objects.all().last())
            player2.save()
        if form3.is_valid():
            player3 = Player(first_name=form3.cleaned_data['first_name'], last_name=form3.cleaned_data['last_name'],
                             player_position=form3.cleaned_data['player_position'],
                             country=form3.cleaned_data['country'], team=Team.objects.all().last())
            player3.save()
        if form4.is_valid():
            player4= Player(first_name=form4.cleaned_data['first_name'], last_name=form4.cleaned_data['last_name'],
                             player_position=form4.cleaned_data['player_position'],
                             country=form4.cleaned_data['country'], team=Team.objects.all().last())
            player4.save()
        if form5.is_valid():
            player5 = Player(first_name=form5.cleaned_data['first_name'], last_name=form5.cleaned_data['last_name'],
                             player_position=form5.cleaned_data['player_position'],
                             country=form5.cleaned_data['country'], team=Team.objects.all().last())
            player5.save()
        if form6.is_valid():
            player6 = Player(first_name=form6.cleaned_data['first_name'], last_name=form6.cleaned_data['last_name'],
                             player_position=form6.cleaned_data['player_position'],
                             country=form6.cleaned_data['country'], team=Team.objects.all().last())
            player6.save()
        if form7.is_valid():
            player7 = Player(first_name=form7.cleaned_data['first_name'], last_name=form7.cleaned_data['last_name'],
                             player_position=form7.cleaned_data['player_position'],
                             country=form7.cleaned_data['country'], team=Team.objects.all().last())
            player7.save()
        if form8.is_valid():
            player8 = Player(first_name=form8.cleaned_data['first_name'], last_name=form8.cleaned_data['last_name'],
                             player_position=form8.cleaned_data['player_position'],
                             country=form8.cleaned_data['country'], team=Team.objects.all().last())
            player8.save()
        if form9.is_valid():
            player9 = Player(first_name=form9.cleaned_data['first_name'], last_name=form9.cleaned_data['last_name'],
                             player_position=form9.cleaned_data['player_position'],
                             country=form9.cleaned_data['country'], team=Team.objects.all().last())
            player9.save()
        if form10.is_valid():
            player10 = Player(first_name=form10.cleaned_data['first_name'], last_name=form10.cleaned_data['last_name'],
                             player_position=form10.cleaned_data['player_position'],
                             country=form10.cleaned_data['country'], team=Team.objects.all().last())
            player10.save()
        if form11.is_valid():
            player11 = Player(first_name=form11.cleaned_data['first_name'], last_name=form11.cleaned_data['last_name'],
                             player_position=form11.cleaned_data['player_position'],
                             country=form11.cleaned_data['country'], team=Team.objects.all().last())
            player11.save()
            return HttpResponseRedirect('team_create')
    else:
        form1 = CreatePlayers(prefix="form1")
        form2 = CreatePlayers(prefix="form2")
        form3 = CreatePlayers(prefix="form3")
        form4 = CreatePlayers(prefix="form4")
        form5 = CreatePlayers(prefix="form5")
        form6 = CreatePlayers(prefix="form6")
        form7 = CreatePlayers(prefix="form7")
        form8 = CreatePlayers(prefix="form8")
        form9 = CreatePlayers(prefix="form9")
        form10 = CreatePlayers(prefix="form10")
        form11 = CreatePlayers(prefix="form11")

    return render(request, 'players-create.html',
                  {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                   'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11})
