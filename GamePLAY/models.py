import pytz as pytz
from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    stadium_name = models.CharField(max_length=50)
    coach_name = models.CharField(max_length=50)
    creation_date = models.DateField(null=True)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.team_name


class League(models.Model):
    league_name = models.CharField(max_length=50)

    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team2')
    team3 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team3')
    team4 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team4')
    team5 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team5')
    team6 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team6')
    team7 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team7')
    team8 = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team8')

    class Meta:
        verbose_name = "League"
        verbose_name_plural = "Leagues"

    def __str__(self):
        return str(self.league_name)


class Player(models.Model):
    PLAYER_POSITION = [
        ('GK', 'Goalkeeper'),
        ('CB', 'Defender'),
        ('CM', 'Midfielder'),
        ('ST', 'Striker'),
    ]

    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(null=True)
    player_position = models.CharField(max_length=10, choices=PLAYER_POSITION, default='')
    country = models.CharField(max_length=50, choices=pytz.country_names.items(), blank=True)
    number_of_goals = models.PositiveIntegerField(default=0)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_team')
    match_date = models.DateTimeField(null=True)
    queue_number = models.PositiveIntegerField()
    match_score = models.CharField(max_length=5, blank=True, default='-')

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.home_team) + " vs " + str(self.visiting_team)


class PlayerStatistic(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, default='', related_name='match')
    player_name = models.ForeignKey(Player, on_delete=models.CASCADE, default='', related_name='player_name')
    number_of_goals = models.PositiveIntegerField(default=0)
    number_of_assists = models.PositiveIntegerField(default=0)
    number_of_passes = models.PositiveIntegerField(default=0)
    number_of_fouls = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "PlayerStatistic"
        verbose_name_plural = "PlayerStatistics"

    def __str__(self):
        return str(self.match)


class TeamStatistic(models.Model):
    team_name = models.ForeignKey(Team, on_delete=models.CASCADE, default='', related_name='team_name_in_TeamStatistic')

    # number_of_goals = models.PositiveIntegerField(default=0)
    # number_of_passes = models.PositiveIntegerField(default=0)
    # number_of_fouls = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "TeamStatistic"
        verbose_name_plural = "TeamStatistics"

    def __str__(self):
        return str(self.match)
