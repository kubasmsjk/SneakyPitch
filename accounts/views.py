from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.utils import timezone


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
            team = Team(team_name=form.cleaned_data['team_name'], stadium_name=form.cleaned_data['stadium_name'],
                        coach_name=form.cleaned_data['coach_name'],
                        creation_date=form.cleaned_data['creation_date'], league_name=form.cleaned_data['league_name'],
                        add_by=request.user.username)
            team.save()
        else:
            if datetime.datetime.strptime(request.POST['creation_date'], '%Y-%m-%d') >= timezone.datetime.today():
                return HttpResponseRedirect('team_create', messages.error(request, "Invalid date."))
            else:
                return HttpResponseRedirect('team_create', messages.error(request, "This team exist."))
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
                             country=form1.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player1.save()
        if form2.is_valid():
            player2 = Player(first_name=form2.cleaned_data['first_name'], last_name=form2.cleaned_data['last_name'],
                             player_position=form2.cleaned_data['player_position'],
                             country=form2.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player2.save()
        if form3.is_valid():
            player3 = Player(first_name=form3.cleaned_data['first_name'], last_name=form3.cleaned_data['last_name'],
                             player_position=form3.cleaned_data['player_position'],
                             country=form3.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player3.save()
        if form4.is_valid():
            player4 = Player(first_name=form4.cleaned_data['first_name'], last_name=form4.cleaned_data['last_name'],
                             player_position=form4.cleaned_data['player_position'],
                             country=form4.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player4.save()
        if form5.is_valid():
            player5 = Player(first_name=form5.cleaned_data['first_name'], last_name=form5.cleaned_data['last_name'],
                             player_position=form5.cleaned_data['player_position'],
                             country=form5.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player5.save()
        if form6.is_valid():
            player6 = Player(first_name=form6.cleaned_data['first_name'], last_name=form6.cleaned_data['last_name'],
                             player_position=form6.cleaned_data['player_position'],
                             country=form6.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player6.save()
        if form7.is_valid():
            player7 = Player(first_name=form7.cleaned_data['first_name'], last_name=form7.cleaned_data['last_name'],
                             player_position=form7.cleaned_data['player_position'],
                             country=form7.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player7.save()
        if form8.is_valid():
            player8 = Player(first_name=form8.cleaned_data['first_name'], last_name=form8.cleaned_data['last_name'],
                             player_position=form8.cleaned_data['player_position'],
                             country=form8.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player8.save()
        if form9.is_valid():
            player9 = Player(first_name=form9.cleaned_data['first_name'], last_name=form9.cleaned_data['last_name'],
                             player_position=form9.cleaned_data['player_position'],
                             country=form9.cleaned_data['country'],
                             team=Team.objects.all().filter(add_by=request.user.username).last())
            player9.save()
        if form10.is_valid():
            player10 = Player(first_name=form10.cleaned_data['first_name'], last_name=form10.cleaned_data['last_name'],
                              player_position=form10.cleaned_data['player_position'],
                              country=form10.cleaned_data['country'],
                              team=Team.objects.all().filter(add_by=request.user.username).last())
            player10.save()
        if form11.is_valid():
            player11 = Player(first_name=form11.cleaned_data['first_name'], last_name=form11.cleaned_data['last_name'],
                              player_position=form11.cleaned_data['player_position'],
                              country=form11.cleaned_data['country'],
                              team=Team.objects.all().filter(add_by=request.user.username).last())
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


@login_required(login_url='main')
def enter_results(request, user=None, id=None, home_team=None, away_team=None):
    match_objects = Match.objects.all().filter(match_date__lt=datetime.datetime.now(), status=False,
                                               home_team__add_by=request.user).order_by('match_date')

    home_team = request.GET.get("home_team")
    away_team = request.GET.get("away_team")
    if request.method == "POST":

        id = request.GET.get("id")
        instance = get_object_or_404(Match, id=id)
        form1 = MatchScore(request.POST, instance=instance)
        form2 = HomePlayersMatchStatistic(request.POST, home_team=home_team, prefix="form2")
        form3 = AwayPlayersMatchStatistic(request.POST, away_team=away_team, prefix="form3")

        if form1.is_valid():
            form1.save()

        if form2.is_valid():
            player_id = request.POST.get('form2-player')
            home_player = PlayerStatistic.objects.all().filter(player_id=player_id).update(
                team_name=home_team,
                number_of_goals=request.POST.get('form2-number_of_goals'),
                number_of_assists=request.POST.get('form2-number_of_assists'),
                number_of_fouls=request.POST.get('form2-number_of_fouls'),
                card=request.POST.get('form2-card'))

            player_id = request.POST.get('form2-player0')
            home_player1 = PlayerStatistic.objects.all().filter(player_id=player_id).update(
                team_name=home_team,
                number_of_goals=request.POST.get('form2-number_of_goals0'),
                number_of_assists=request.POST.get('form2-number_of_assists0'),
                number_of_fouls=request.POST.get('form2-number_of_fouls0'),
                card=request.POST.get('form2-card0'))

            player_id = request.POST.get('form2-player1')
            home_player2 = PlayerStatistic.objects.all().filter(player_id=player_id).update(
                team_name=home_team,
                number_of_goals=request.POST.get('form2-number_of_goals1'),
                number_of_assists=request.POST.get('form2-number_of_assists1'),
                number_of_fouls=request.POST.get('form2-number_of_fouls1'),
                card=request.POST.get('form2-card1'))

        if form3.is_valid():
            player_id = request.POST.get('form3-player')
            away_player = PlayerStatistic.objects.all().filter(player_id=player_id).update(
                team_name=away_team,
                number_of_goals=request.POST.get('form3-number_of_goals'),
                number_of_assists=request.POST.get('form3-number_of_assists'),
                number_of_fouls=request.POST.get('form3-number_of_fouls'),
                card=request.POST.get('form3-card'))
            player_id = request.POST.get('form3-player0')
            away_player1 = PlayerStatistic.objects.all().filter(player_id=player_id).update(
                team_name=away_team,
                number_of_goals=request.POST.get('form3-number_of_goals0'),
                number_of_assists=request.POST.get('form3-number_of_assists0'),
                number_of_fouls=request.POST.get('form3-number_of_fouls0'),
                card=request.POST.get('form3-card0'))
            return HttpResponseRedirect('/')
    else:
        form1 = MatchScore()
        form2 = HomePlayersMatchStatistic(home_team=home_team, prefix="form2")
        form3 = AwayPlayersMatchStatistic(away_team=away_team, prefix="form3")

    return render(request, 'enter-the-results.html',
                  {'form1': form1, 'form2': form2, 'form3': form3, 'match_objects': match_objects})
