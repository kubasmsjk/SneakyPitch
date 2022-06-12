import pytz as pytz
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import datetime


class League(models.Model):
    league_name = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = "League"
        verbose_name_plural = "Leagues"

    def clean(self):
        if League.objects.filter(league_name=self.league_name).exists():
            raise ValidationError("Error: This league exist.")

    def __str__(self):
        return str(self.league_name)


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    stadium_name = models.CharField(max_length=50)
    coach_name = models.CharField(max_length=50)
    creation_date = models.DateField(null=True)
    game_played = models.PositiveIntegerField(default=0)
    number_of_goals_diffrence = models.IntegerField(default=0)
    number_of_points = models.PositiveIntegerField(default=0)
    league_name = models.ForeignKey(League, on_delete=models.CASCADE, default='')
    add_by = models.CharField(max_length=50)

    def clean(self):
        if Team.objects.filter(team_name=self.team_name).exists():
            raise ValidationError("Error: This team exist.")
        if self.creation_date > datetime.date.today():
            raise ValidationError('Error: invalid date.')

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.team_name


@receiver(post_save, sender=Team)
def create_team_statistic(instance, created, **kwargs):
    if created:
        TeamStatistic.objects.create(team_name=instance.team_name, number_of_points=instance.number_of_points)

@receiver(post_delete, sender=Team)
def delete_player_statistic(instance, **kwargs):
    TeamStatistic.objects.filter(team_name=instance.team_name).delete()

class Player(models.Model):
    PLAYER_POSITION = [
        ('GK', 'Goalkeeper'),
        ('CB', 'Defender'),
        ('CM', 'Midfielder'),
        ('ST', 'Striker'),
    ]
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    player_position = models.CharField(max_length=10, choices=PLAYER_POSITION, default='')
    country = models.CharField(max_length=50, choices=pytz.country_names.items(), blank=True, default='')
    number_of_goals = models.PositiveIntegerField(default=0)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default='')
    link = "Edit"

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)

@receiver(post_delete, sender=Player)
def delete_player_statistic(instance, **kwargs):
    PlayerStatistic.objects.filter(pk=instance.pk).delete()


class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    match_date = models.DateTimeField(null=True)
    queue_number = models.PositiveIntegerField()
    home_team_goals = models.PositiveIntegerField(default='0')
    away_team_goals = models.PositiveIntegerField(default='0')
    status = models.BooleanField(default=False)

    def clean(self):
        if self.home_team == self.away_team:
            raise ValidationError("Error: Two teams with the same name.")

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.home_team) + " vs " + str(self.away_team)


class PlayerStatistic(models.Model):
    PLAYER_CARD = [
        ('--', '------'),
        ('YE', 'Yellow'),
        ('RE', 'Red'),
    ]
    player = models.ForeignKey(Player, on_delete=models.CASCADE, default='')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, default='')
    team_name = models.CharField(max_length=50, blank=True, default='')
    number_of_goals = models.PositiveIntegerField(default=0)
    number_of_assists = models.PositiveIntegerField(default=0)
    number_of_fouls = models.PositiveIntegerField(default=0)
    card = models.CharField(max_length=10, choices=PLAYER_CARD, default='')

    class Meta:
        verbose_name = "PlayerStatistic"
        verbose_name_plural = "PlayerStatistics"

@receiver(post_save, sender=PlayerStatistic)
def update_Player(sender, instance, created, **kwargs):
    if created:
        Player.objects.filter(pk=instance.pk).update(number_of_goals=instance.number_of_goals)


class TeamStatistic(models.Model):
    team_name = models.CharField(max_length=50, blank=True, default='')
    game_played = models.PositiveIntegerField(default=0)
    number_of_win = models.PositiveIntegerField(default=0)
    number_of_draw = models.PositiveIntegerField(default=0)
    number_of_losses = models.PositiveIntegerField(default=0)
    number_of_goals_for = models.PositiveIntegerField(default=0)
    number_of_goals_against = models.PositiveIntegerField(default=0)
    number_of_goals_diffrence = models.IntegerField(default=0)
    number_of_points = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "TeamStatistic"
        verbose_name_plural = "TeamStatistics"


class StaticItems(models.Model):
    main_background_image = models.ImageField(blank=True, null=True)
    contact_us_background_image = models.ImageField(blank=True, null=True)
    link = "Edit"

    class Meta:
        verbose_name = "StaticItem"
        verbose_name_plural = "StaticItems"


class Search(models.Model):
    address = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.address
