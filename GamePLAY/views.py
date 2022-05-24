<<<<<<< HEAD
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import SearchForm
from .models import *
from .models import Search
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
import folium
import geocoder
=======
from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
>>>>>>> c6bc06a117a85235b167be8f9a42765bfd07e4f1


# Create your views here.
def main_view(request):
    static_items = StaticItems.objects.all()
    #map
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    m = folium.Map(location=[40,-4], zoom_start=5)
    folium.Marker([lat, lng], tooltip ='Click', popup=country).add_to(m)
    m = m._repr_html_()
    dane_items = {'static_items': static_items,
                  'm': m,
                  'form': form,
                  }
    #mail
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if (email == '' or subject == '' or message == ''):
            messages.success(request, "Fields cannot be empty")
        else:
            send_mail(subject, message, email, ['jakm5000@wp.pl'])
<<<<<<< HEAD

=======
>>>>>>> c6bc06a117a85235b167be8f9a42765bfd07e4f1
    return render(request, 'main.html', dane_items)


def tables_view(request):
    team_objects = Team.objects.all().order_by('-points')
    context = {
        'team_objects': team_objects
    }
    return render(request, 'tables.html', context)


def queues_view(request):
    queue_objects = Match.objects.all().order_by('queue_number', 'match_date')
    dane_queue = {'queue_objects': queue_objects}
    return render(request, 'queues.html', dane_queue)


def teams_view(request):
    team_objects = Team.objects.all()
    dane_team = {'team_objects': team_objects}

    return render(request, 'teams.html', dane_team)


def shooters_rank_view(request):
    player_rank = Player.objects.all().order_by('-number_of_goals')[:10]
    context = {
        'player_rank': player_rank
    }

    return render(request, 'shootersRank.html', context)
