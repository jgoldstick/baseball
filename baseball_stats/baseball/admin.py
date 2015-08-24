from django.contrib import admin
from .models import Master, TeamFranchise, HallOfFame, League, Team, Salary
from .models import Batting, Pitching, Fielding, Appearances, Manager, PostSeasonSeries

# Register your models here.


class MasterAdmin(admin.ModelAdmin):
    list_display = ("name_last", "name_first", 'birth_city', 'birth_state',
                    'birth_country', 'debut', 'final_game')
    list_filter = ("birth_country", 'debut')
    search_fields = ('name_last', 'name_first')

admin.site.register(Master, MasterAdmin)


class PostSeasonSeriesAdmin(admin.ModelAdmin):
    list_display = ("year", "playoff_round", "team_winner", "league_winner", "team_loser", "league_loser", "wins", "losses", "ties")
    list_filter = ("playoff_round", "league_winner", "league_loser", "year")
    # list_display = ("pk", "year", "playoff_round",  "wins", "losses", "ties")
admin.site.register(PostSeasonSeries, PostSeasonSeriesAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'team', 'franchise', 'league', 'park_name', 'year')
    list_filter = ('league', 'franchise', 'year')

admin.site.register(Team, TeamAdmin)


class SalaryAdmin(admin.ModelAdmin):
    list_display = ('player', 'team', 'year', 'salary')
    search_fields = ('player__name_last',)

admin.site.register(Salary, SalaryAdmin)


class TeamFranchiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'na_association')

admin.site.register(TeamFranchise, TeamFranchiseAdmin)


class HallOfFameAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'voted_by', 'votes_needed', 'votes_received', 'percent_vote', 'inducted', 'category')
    list_filter = ('inducted',)
    search_fields = ('player__name_last', 'player__name_first')

admin.site.register(HallOfFame, HallOfFameAdmin)


class LeagueAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name')

admin.site.register(League, LeagueAdmin)


class BattingAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'stint', 'team', 'games_batting', 'homeruns', 'league')
    # list_filter = ('player', 'year', 'team')
    search_fields = ('player__name_last', 'team')

admin.site.register(Batting, BattingAdmin)


class PitchingAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'stint', 'team', 'league')
    # list_filter = ('player', 'year', 'team')
    search_fields = ('player__name_last', 'team')

admin.site.register(Pitching, PitchingAdmin)


class FieldingAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'stint', 'team', 'league')
    # list_filter = ('player', 'year', 'team')
    search_fields = ('player__name_last', 'team')

admin.site.register(Fielding, FieldingAdmin)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('manager', 'year', 'in_season', 'won', 'lost', 'team',
                    'league', 'player_manager')
    list_filter = ('year', 'team')
    # search_fields = ('manager__name_last', 'team')

admin.site.register(Manager, ManagerAdmin)


class AppearancesAdmin(admin.ModelAdmin):
    list_display = ('player', 'year', 'team', 'league')
    list_filter = ('year', 'team__team')
    search_fields = ('player__name_last', 'team')

admin.site.register(Appearances, AppearancesAdmin)
