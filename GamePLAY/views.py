from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def main_view(request):
    static_items = StaticItems.objects.all()
    dane_items = {'static_items': static_items}
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if (email == '' or subject == '' or message == ''):
            messages.success(request, "Fields cannot be empty")
        else:
            send_mail(subject, message, email, ['jakm5000@wp.pl'])
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
