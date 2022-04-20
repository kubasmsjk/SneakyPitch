from django.contrib import admin
from .models import Player, Team, Match


# Register your models here.

class PlayerInLIne(admin.StackedInline):
    model=Player



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'player_position', 'team']
    list_filter = ['team']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['team_name', 'stadium_name', 'coach_name', 'creation_date']
    inlines = [
        PlayerInLIne
    ]



@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    search_fields = ['home_team__team_name','visiting_team__team_name']
    list_display = ['home_team', 'visiting_team', 'match_date', 'queue_number', 'match_score']
