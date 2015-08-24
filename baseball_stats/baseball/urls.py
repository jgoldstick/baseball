from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('baseball.views',
    url(r'^batting/$', 'batting', {'domain': 'batting'}, name='batting'),
    url(r'^pitching/$', 'pitching', {'domain': 'pitching'}, name='pitching'),
    url(r'^fielding/$', 'fielding', {'domain': 'fielding'}, name='fielding'),
    url(r'^teams/$', 'teams', name='teams'),
    url(r'^teams/active/$', 'active_franchises', name='active_franchises'),
    url(r'^teams/inactive/$', 'inactive_franchises', name='inactive_franchises'),
    url(r'^team/(?P<team_id>\d{4}\w{3})/$', 'team_year', name='team_year'),
    url(r'^team_history/(?P<franchise>\w{3})/$', 'team_history', name='team_history'),
    url(r'^teams/$', 'teams', name='teams'),
    url(r'^teams/(?P<year>\d{4})/$', 'teams', name='teams'),
    url(r'^players/$', 'players', name='players'),
    url(r'^players/(?P<last_name>\w+)/$', 'players', name='players'),
    url(r'^players/(?P<birth_country>)/$', 'players', name='players'),
    url(r'^player_card/(?P<player_id>\w+)/$', 'player_card', name='player_card'),
    url(r'^hall/$', 'hall', name='hall'),
    url(r'^hall_by_year/$', 'hall_by_year', name='hall_by_year'),
    url(r'^birthdays/$', 'birthdays', name='birthday'),
    url(r'^birthdays/(?P<month>\d{1,2})/(?P<date>\d{1,2})/$', 'birthdays', name='birthday'),
    url(r'^birth_country/$', 'birth_country', name='birth_country'),
    url(r'^birth_country_by_year/$', 'birth_country_by_year', name='birth_country_by_year'),
    url(r'^post_season/$', 'post_season', name='post_season'),
)
