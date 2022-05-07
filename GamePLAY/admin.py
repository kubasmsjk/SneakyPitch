from django.contrib import admin
from .models import *

# Register your models here.

class PlayerInLIne(admin.StackedInline):
    model = Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'player_position', 'team','number_of_goals']
    list_filter = ['team']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'stadium_name', 'coach_name', 'creation_date', 'points']
    inlines = [
        PlayerInLIne
    ]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    search_fields = ['home_team__team_name', 'visiting_team__team_name']
    list_display = ['home_team', 'visiting_team', 'match_date', 'queue_number', 'match_score']


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['league_name']


@admin.register(PlayerStatistic)
class PlayerStatisticAdmin(admin.ModelAdmin):
    list_display = ['match', 'player_name', 'number_of_goals', 'number_of_assists', 'number_of_passes',
                    'number_of_fouls']


@admin.register(TeamStatistic)
class TeamStatisticAdmin(admin.ModelAdmin):
    pass

@admin.register(StaticItems)
class StaticItems(admin.ModelAdmin):
    list_display = ['main_background_image', 'link']
    list_display_links = ['link']
    list_editable = ['main_background_image']

