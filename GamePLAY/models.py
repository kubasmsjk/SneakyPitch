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
    points = models.IntegerField(default=0)
    league_name = models.ForeignKey(League, on_delete=models.CASCADE, default='')

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
        TeamStatistic.objects.create(team_name=instance.team_name)


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
    link = "Edit"

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


@receiver(post_save, sender=Player)
def create_player_statistic(instance, created, **kwargs):
    if created:
        PlayerStatistic.objects.create(player_name=instance.first_name, team_name=instance.team.team_name)


@receiver(post_delete, sender=Player)
def delete_player_statistic(instance, **kwargs):
    PlayerStatistic.objects.filter(player_name=instance.first_name, team_name=instance.team.team_name).delete()


class Match(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    match_date = models.DateTimeField(null=True)
    queue_number = models.PositiveIntegerField()
    home_team_goals = models.PositiveIntegerField(default='0')
    away_team_goals = models.PositiveIntegerField(default='0')

    def clean(self):
        if self.home_team == self.away_team:
            raise ValidationError("Error: Two teams with the same name.")
        if self.match_date.date() <= datetime.date.today():
            raise ValidationError('Error: invalid date.')

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.home_team) + " vs " + str(self.away_team)


class PlayerStatistic(models.Model):
    player_name = models.CharField(max_length=50, blank=True, default='')
    team_name = models.CharField(max_length=50, blank=True, default='')
    home_team = models.CharField(max_length=50, blank=True, default='')
    away_team = models.CharField(max_length=50, blank=True, default='')
    number_of_goals = models.PositiveIntegerField(default=0)
    number_of_assists = models.PositiveIntegerField(default=0)
    number_of_passes = models.PositiveIntegerField(default=0)
    number_of_fouls = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "PlayerStatistic"
        verbose_name_plural = "PlayerStatistics"


@receiver(post_save, sender=Player)
def make_PlayerStatistic(sender, instance, **kwargs):
    PlayerStatistic.objects.filter(player_name=instance.first_name).update(player_name=instance.first_name,
                                                                           number_of_goals=instance.number_of_goals)


class TeamStatistic(models.Model):
    team_name = models.CharField(max_length=50, blank=True, default='')
    number_of_goals = models.PositiveIntegerField(default=0)
    number_of_passes = models.PositiveIntegerField(default=0)
    number_of_fouls = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "TeamStatistic"
        verbose_name_plural = "TeamStatistics"


# @receiver(post_save, sender=PlayerStatistic)
# def make_TeamStatistic(sender, instance, created, **kwargs):
#   if created:
#      TeamStatistic.objects.update(team_name=instance.team_name,number_of_goals=instance.number_of_goals,number_of_passes=instance.number_of_passes,number_of_fouls=instance.number_of_fouls)


class StaticItems(models.Model):
    main_background_image = models.ImageField(blank=True, null=True)
    contact_us_background_image = models.ImageField(blank=True, null=True)
    link = "Edit"

    class Meta:
        verbose_name = "StaticItem"
        verbose_name_plural = "StaticItems"

class Search(models.Model):
    address = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address