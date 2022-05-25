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
            return HttpResponseRedirect('team_create')
    else:
        form = CreateTeam

    if request.method == "POST":
        form_two = CreatePlayers(request.POST)
        if form_two.is_valid():
            form_two.save()
            return HttpResponseRedirect('team_create')
    else:
        form_two = CreatePlayers
    return render(request, 'team-create.html', {'form': form, 'form_two': form_two})
