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
            form1.save()
        if form2.is_valid():
            form2.save()
        if form3.is_valid():
            form3.save()
        if form4.is_valid():
            form4.save()
        if form5.is_valid():
            form5.save()
        if form6.is_valid():
            form6.save()
        if form7.is_valid():
            form7.save()
        if form8.is_valid():
            form8.save()
        if form9.is_valid():
            form9.save()
        if form10.is_valid():
            form10.save()
        if form11.is_valid():
            form11.save()
            return HttpResponseRedirect('team_create')
    else:
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

    return render(request, 'players-create.html',
                  {'form1': form1, 'form2': form2, 'form3': form3, 'form4': form4, 'form5': form5, 'form6': form6,
                   'form7': form7, 'form8': form8, 'form9': form9, 'form10': form10, 'form11': form11})
