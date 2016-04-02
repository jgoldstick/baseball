from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^batting/$', views.aggregate_category, {'domain': 'batting'}, name='batting'),
    url(r'^pitching/$', views.aggregate_category, {'domain': 'pitching'}, name='pitching'),
    url(r'^fielding/$', views.aggregate_category, {'domain': 'fielding'}, name='fielding'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/active/$', views.active_franchises, name='active_franchises'),
    url(r'^teams/inactive/$', views.inactive_franchises, name='inactive_franchises'),
    url(r'^team/(?P<team_id>\d{4}\w{3})/$', views.team_year, name='team_year'),
    url(r'^team_history/(?P<franchise>\w{3})/$', views.team_history, name='team_history'),
    url(r'^teams/$', views.teams, name='teams'),
    url(r'^teams/(?P<year>\d{4})/$', views.teams, name='teams'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/(?P<last_name>\w+)/$', views.players, name='players'),
    url(r'^players/(?P<birth_country>)/$', views.players, name='players'),
    url(r'^player_card/(?P<player_id>\w+)/$', views.player_card, name='player_card'),
    url(r'^hall/$', views.hall, name='hall'),
    url(r'^hall_by_year/$', views.hall_by_year, name='hall_by_year'),
    url(r'^birthdays/$', views.birthdays, name='birthday'),
    url(r'^birthdays/(?P<month>\d{1,2})/(?P<date>\d{1,2})/$', views.birthdays, name='birthday'),
    url(r'^birth_country/$', views.birth_country, name='birth_country'),
    url(r'^birth_country_by_year/$', views.birth_country_by_year, name='birth_country_by_year'),
    url(r'^post_season/$', views.post_season, name='post_season'),
    url(r'^chart/$', views.chart, name='chart'),
]

