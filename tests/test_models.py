from django.test import TestCase
from GamePLAY.models import League, Team, Player, Match
from django.core.exceptions import ValidationError



class LeagueModelTestCase(TestCase):
    def setUp(self):
        league1 = self.league = League(league_name='diga')
        self.assertEqual(str(league1), 'diga')

    def test_league_creation(self):
        self.league.save()
        self.assertIsNotNone(self.league.id)

    def test_league_model_validation(self):
        league2 = League.objects.create(league_name='diga')
        with self.assertRaises(ValidationError):
            instance = League(league_name='diga')
            instance.clean()

class TeamModelTestCase(TestCase):

    def setUp(self):
            league = League.objects.create(league_name='test_team_league_name')
            mieko = self.team = Team(team_name='FC mieko', stadium_name='Miekowo Arena', coach_name='Jerzy Dudek', creation_date='2020-12-12',
                             game_played=3, number_of_goals_diffrence=5, number_of_points=12, league_name=league, add_by='Miekulec')
            self.assertEqual(str(mieko.coach_name), 'Jerzy Dudek')

    def test_team_creation(self):
            self.team.save()
            self.assertIsNotNone(self.team.id)

class PlayerModelTestCase(TestCase):

    def setUp(self):

        league = League.objects.create(league_name='test_team_league_name')
        team_test = self.team = Team(team_name='FC mieko', stadium_name='Miekowo Arena', coach_name='Jerzy Dudek',
                                 creation_date='2020-12-12',
                                 game_played=3, number_of_goals_diffrence=5, number_of_points=12, league_name=league,
                                 add_by='Miekulec')
        #player create
        player = self.player = Player(first_name='Adam', last_name='Nierób', player_position='Goalkeeper',
                                      number_of_goals='0', team=team_test)
        self.assertEqual(str(player.player_position), 'Goalkeeper')

    def test_player_creation(self):
        self.team.save()
        self.player.save()
        self.assertIsNotNone(self.player.id)

class MatchModelTestCase(TestCase):

    def setUp(self):
        league = League.objects.create(league_name='test_team_league_name')
        home_team_test = self.team = Team(team_name='FC mieko', stadium_name='Miekowo Arena', coach_name='Jerzy Dudek',
                                     creation_date='2020-12-12',
                                     game_played=3, number_of_goals_diffrence=5, number_of_points=12,
                                     league_name=league,add_by='Miekulec')



        match_test = self.match = Match(home_team=home_team_test, away_team=home_team_test, match_date='2021-12-12', queue_number='5', home_team_goals=5,
                                        away_team_goals=4, status=False)

        self.assertEqual(str(match_test.queue_number), '5')

    def test_match_creation(self):
        self.team.save()
        self.match.save()
        self.assertIsNotNone(self.match.id)