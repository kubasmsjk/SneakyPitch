from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import *
from django.core.mail import send_mail
from smtplib import SMTPException
import folium
import geocoder
from django.contrib import messages


# Create your views here.
def main_view(request):
    static_items = StaticItems.objects.all()
    # map
    if 'find' in request.POST and request.method == 'POST':
        form_map = SearchForm(request.POST)
        if form_map.is_valid():
            form_map.save()
            return redirect('/' + "#section-1")
    else:
        form_map = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat is None or lng is None:
        address.delete()
        return redirect('/' + "#base", messages.error(request, "This Club doesn't exist, try again"))
    m = folium.Map(location=[lat, lng], zoom_start=7.0)
    folium.Marker([lat, lng], tooltip='Click', popup=country,
                  icon=folium.Icon(color='red', icon='futbol-o', prefix='fa')).add_to(m)
    m = m._repr_html_()
    context = {'static_items': static_items,
               'm': m,
               'form_map': form_map,
               }
    # mail
    if 'contact' in request.POST and request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if email == '' or subject == '' or message == '':
            messages.error(request, "Fields cannot be empty")
            return redirect('/' + '#base')
        else:
            try:
                send_mail(subject, message, email, ['jakm5000@wp.pl'], fail_silently=False)
            except SMTPException:
                return redirect('/' + '#base', messages.error(request, "Invalid header found."))
            return redirect('/' + '#base', messages.success(request, "Thank you for your email"))
    return render(request, 'main.html', context)


def tables_view(request):
    team_objects = Team.objects.all().order_by('-number_of_points')
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

    return render(request, 'shooters-rank.html', context)


def team_statistic_view(request):
    team_statistic = TeamStatistic.objects.all()
    context = {
        'team_statistic': team_statistic
    }

    return render(request, 'team-statistic.html', context)


def player_statistic_view(request):
    player_statistic = PlayerStatistic.objects.all()
    context = {
        'player_statistic': player_statistic
    }

    return render(request, 'player-statistic.html', context)

