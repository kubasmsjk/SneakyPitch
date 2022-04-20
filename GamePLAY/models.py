import pytz as pytz
from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    stadium_name = models.CharField(max_length=50)
    coach_name = models.CharField(max_length=50)
    creation_date = models.DateField(null=True)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.team_name


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
    number_of_goals = models.IntegerField(default=0)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, default='')

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    visiting_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='visiting_team')
    match_date = models.DateField(null=True)
    queue_number = models.IntegerField()
    match_score = models.CharField(max_length=5, blank=True)

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return self.home_team