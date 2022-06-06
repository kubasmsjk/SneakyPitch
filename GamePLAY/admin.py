from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Search)


class PlayerInLIne(admin.StackedInline):
    model = Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'player_position', 'country', 'team', 'number_of_goals',
                    'link']
    list_filter = ['team']
    list_display_links = ['link']
    list_editable = ['first_name', 'last_name', 'player_position', 'team', 'number_of_goals']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'stadium_name', 'coach_name', 'creation_date', 'game_played',
                    'number_of_goals_diffrence', 'number_of_points', 'league_name',
                    'add_by']
    inlines = [
        PlayerInLIne
    ]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    search_fields = ['home_team__team_name', 'away_team__team_name']
    list_display = ['home_team', 'away_team', 'match_date', 'queue_number', 'home_team_goals', 'away_team_goals',
                    'status']


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['league_name']


@admin.register(PlayerStatistic)
class PlayerStatisticAdmin(admin.ModelAdmin):
    list_display = ['player', 'team_name', 'number_of_goals', 'number_of_assists',
                    'number_of_fouls', 'card']


@admin.register(TeamStatistic)
class TeamStatisticAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'game_played', 'number_of_win',
                    'number_of_draw', 'number_of_losses', 'number_of_goals_for', 'number_of_goals_against',
                    'number_of_goals_diffrence', 'number_of_points']


@admin.register(StaticItems)
class StaticItems(admin.ModelAdmin):
    list_display = ['main_background_image', 'contact_us_background_image', 'link']
    list_display_links = ['link']
    list_editable = ['main_background_image', 'contact_us_background_image']
