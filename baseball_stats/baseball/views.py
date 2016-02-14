import datetime
from django.shortcuts import render_to_response
from django.db.models import Max, Sum, Count
#from django.conf import settings
from baseball.models import HallOfFame, Team, Batting, Pitching, Fielding
from baseball.models import Master, PostSeasonSeries, TeamFranchise
from baseball.forms import BattingFilterForm, PitchingFilterForm, FieldingFilterForm
from baseball.forms import BirthdayForm, BirthCountryForm, PlayersForm

def filtered_data_set(data_set, **kwargs):
    """
    returns all data from a model filtered by the attribute values passed as a dictionary
    """
    for k, v in kwargs.items():
        data_set = data_set.objects.filter(**kwargs)

    return data_set


def all_time_(model, category_name, list_size=None):
    """
    generic query returns a ValueQueryset of player name and category sum
    in descending order of length list_size
    """
    if category_name == 'avg':
        """
        get hits and at bats.  c
        """
        data_set = model.objects.values('player', 'player__name_first',
                            'player__name_last').annotate(at_bats=Sum('at_bats'),
                            hits=Sum('hits')).filter(at_bats__gt=500).order_by('-hits')
        for d in data_set:
            try:
                d['category'] = d['hits'] / float(d['at_bats'])
            except ZeroDivisionError:
                d['category'] = 0
        data_set = sorted(data_set, key=lambda k: k['category'], reverse=True)
    elif category_name == 'earned_run_average':
        data_set = model.objects.values('player', 'player__name_first',
                            'player__name_last').annotate(runs =Sum('earned_runs'),
                            outs=Sum('outs_pitched')).filter(outs__gt=270)
        for d in data_set:
            try:
                d['category'] = 27.0 * d['runs'] / d['outs']
            except ZeroDivisionError:
                d['category'] = 999.0
        data_set = sorted(data_set, key=lambda k: k['category'])
    else:
        data_set = model.objects.values('player', 'player__name_first',
                            'player__name_last').annotate(category=Sum(category_name)).order_by('-category')
    if list_size:
        return data_set[:list_size]
    else:
        return data_set


import copy
def batting(request, domain):
    """
    Aggregate query for batting, fielding, pitching depending on domain
    """
    query_filter = dict([(k, v) for k, v in request.GET.items()])
    initial_form_values = copy.deepcopy(query_filter)
    category = query_filter.pop('category', None)

    if domain == 'batting':
        model = Batting
        if not category:
            category = 'at_bats'
        FilterForm = BattingFilterForm
    elif domain == 'pitching':
        model = Pitching
        FilterForm = PitchingFilterForm
        if not category:
            category = "balks"
    elif domain == 'fielding':
        model = Fielding
        FilterForm = FieldingFilterForm
        if not category:
            category = "assists"

    if initial_form_values:
        selected_form = FilterForm(initial_form_values)
    else:
        selected_form = FilterForm()

    if category:
        category_verbose = category.replace("_", " ")

    if query_filter:
        if query_filter['team__franchise'] == "All":
            query_filter.pop('team__franchise')

        if query_filter['year'] == "All":
            query_filter.pop('year')

        if query_filter['league'] == "All":
            query_filter.pop('league')

    data_set = filtered_data_set(model, **query_filter)
    data_set = all_time_(data_set, category, 50)
    context = {'batting': batting,
               'data_set' :  data_set[:50],
               'category' : category_verbose
               }
    context.update(query_filter)
    context.update({'form': selected_form})
    return render_to_response('baseball/batting.html', context)

# pitching and fielding are synonyms for pitching
pitching = batting
fielding = batting

def home(request):
    pass

def birth_country(request):
    countries = Master.objects.values('birth_country').annotate(num_players=(Count('birth_country'))).order_by('-num_players')
    return render_to_response('baseball/countries.html', {'countries': countries})

def birth_country_by_year(request):
    countries = Master.objects.values('birth_country').annotate(num_players=(Count('birth_country'))).order_by('num_players')
    birth_country_year = BirthCountryForm()
    return render_to_response('baseball/countries.html', {'countries': countries, 'form': birth_country_year})


def birthdays(request, month=None, date=None):
    """
    players born in a given month and day
    """
    query_filter = dict([(k, v) for k, v in request.GET.items()])
    if query_filter:
        selected_form = BirthdayForm(query_filter)
        month = query_filter['month']
        date = query_filter['date']
    else:
        d = datetime.date.today()
        month = d.month
        date = d.day
        selected_form = BirthdayForm({'month': d.month, 'date': d.day})

    born_this_date = Master.objects.filter(birth_month=month, birth_day=date).order_by('birth_year')
    return render_to_response('baseball/birthdays.html', {'born_this_date': born_this_date, 'form': selected_form})

def players(request, last_name=None, country=None):
    """
    list of all players or filter by Birth Country and Year
    """
    player = Master.objects.all().order_by("name_last")
    query_filter = dict([(k, v) for k, v in request.GET.items()])
    if query_filter:
        players_form = PlayersForm(query_filter)
        player = player.filter(**query_filter)
    else:
        player = None
        players_form = PlayersForm()
    if last_name:
        player = player.filter(name_last__startswith = last_name)
    return render_to_response('baseball/players.html', {'player': player, 'form': players_form})

def format_date(year, month, day, fmt):
    if year < 1900:
        return datetime.datetime(2000, month, day).strftime(fmt).replace('2000', str(year))
    else:
        return datetime.datetime(year, month, day).strftime(fmt)


def player_card(request, player_id):
    """
    Player card information view -- pitching, fielding, hitting
    """
    def outs_to_innings(outs):
        return outs / 3 + outs % 3 * .1

    batting = Batting.objects.filter(player=player_id).order_by('year', 'stint')
    pitching = Pitching.objects.filter(player=player_id).order_by('year', 'stint')
    fielding = Fielding.objects.filter(player=player_id).order_by('year', 'stint')
    player = Master.objects.get(id=player_id)
    pitching_totals = pitching.aggregate(Sum('wins'), Sum('losses'), Sum('games'),
                                         Sum('games_started'), Sum('complete_games'),
                                         Sum('shutouts'), Sum('saves'),
                                         Sum('outs_pitched'),
                                         Sum('hits'), Sum('earned_runs'),
                                         Sum('homeruns'), Sum('strikeouts'),
                                         Sum('walks'), Sum('intentional_walks'),
                                         Sum('wild_pitches'), Sum('walks'),
                                         Sum('sac_flies'), Sum('sacs_allowed'),
                                         Sum('batters_faced'), Sum('games_finished'),
                                         Sum('shutouts'), Sum('saves'))

    batting_totals = batting.aggregate(Sum('games_batting'), Sum('at_bats'),
                                       Sum('runs'), Sum('hits'), Sum('doubles'),
                                       Sum('triples'), Sum('homeruns'),
                                       Sum('rbi'), Sum('stolen_bases'),
                                       Sum('caught_stealing'), Sum('walks'),
                                       Sum('strike_outs'), Sum('intentional_walks'),
                                       Sum('hit_by_pitch'), Sum('sac_hits'),
                                       Sum('sac_flies'), Sum('double_plays'),
                                        )
    try:
        batting_totals['ave'] = float(batting_totals['hits__sum']) / batting_totals['at_bats__sum']
    except ZeroDivisionError:
        pass
    except TypeError:
        pass

    try:
        pitching_totals['era'] = 27.0 *  pitching_totals['earned_runs__sum'] / pitching_totals['outs_pitched__sum']
    except ZeroDivisionError:
        pass
    except TypeError:
        pass

    try:
       pitching_totals['innings_pitched'] = outs_to_innings(pitching_totals['outs_pitched__sum'])
    except TypeError:
        pass



    fielding_totals = fielding.aggregate(Sum("games"), Sum("games_started"),
                                         Sum("outs_played"), Sum("putouts"),
                                         Sum("assists"), Sum("errors"),
                                         Sum("double_plays"), Sum("passed_balls"),
                                         Sum("wild_pitches"), Sum("stolen_on"),
                                         Sum("caught_stealing")
                                        )

    born = None
    if player.birth_year and player.birth_month and player.birth_day:
        born = format_date(player.birth_year, player.birth_month, player.birth_day, "%B %-d %Y")
    elif player.birth_year and player.birth_month:
        born = format_date(player.birth_year, player.birth_month, 1, "%B %Y")
    elif player.birth_year:
        born = format_date(player.birth_year, 1, 1, "%Y")

    death = None
    if player.death_year and player.death_month and player.death_day:
        death  = format_date(player.death_year, player.death_month, player.death_day, "%B %-d %Y")
    elif player.death_year and player.death_month:
        death = format_date(player.death_year, player.death_month, 1, "%B %Y")
    elif player.death_year:
        death  = format_date(player.death_year, 1, 1, "%Y")

    hall = HallOfFame.objects.filter(player=player_id).filter(inducted=True)
    if hall:
        hall = hall[0]
    return render_to_response("baseball/player_card.html",
                              {'player':player, 'batting': batting, 'pitching': pitching,
                               'fielding': fielding, 'player_name': player, 'hall': hall,
                               'pitching_totals': pitching_totals,
                               'batting_totals': batting_totals,
                               'fielding_totals': fielding_totals,
                               'born':born, 'death': death})


def teams(request, year=None):
    if not year:
        max_year = Team.objects.all().aggregate(Max('year'))
    else:
        max_year = {}
        max_year['year__max'] = year
    teams = Team.objects.all().filter(year=max_year['year__max']).order_by('league', 'division', 'rank')
    leagues = teams.order_by('league').values_list('league', flat=True).distinct()
    #leagues = teams.values('league').distinct()
    divisions = teams.order_by('division').values_list('division', flat=True).distinct()
    ld ={}
    for l in leagues:
        for d in divisions:
            teams_ld = teams.filter(league=l, division=d)
            ld["".join([l,d])] = teams_ld

    ctx = {'leagues':leagues, 'divisions':divisions, 'year': max_year['year__max']}
    ctx.update(ld)
    return render_to_response('baseball/teams.html', ctx)

def team_year(request, team_id):
    batting = Batting.objects.filter(team=team_id).order_by('-at_bats')
    pitching = Pitching.objects.filter(team=team_id).order_by('-wins')
    fielding = Fielding.objects.filter(team=team_id).order_by('games')
    #team = Team.objects.filter(id=team_id).values()
    team = Team.objects.get(id=team_id)
    return render_to_response('baseball/team_year.html',
                              {'team': team, 'pitching': pitching, 'batting': batting, 'fielding': fielding})

def team_history(request, franchise):
    team_by_year = Team.objects.filter(franchise_id=franchise)
    return render_to_response('baseball/team_history.html', {'teams': team_by_year})

def active_franchises(request):
    franchises = TeamFranchise.objects.filter(active=True)
    return render_to_response('baseball/active_franchises.html', {'franchises': franchises})

def inactive_franchises(request):
    franchises = TeamFranchise.objects.filter(active=False)
    return render_to_response('baseball/inactive_franchises.html', {'franchises': franchises})

def hall(request):
    hall =  HallOfFame.objects.filter(inducted=True, voted_by='BBWAA')
    sorted_hall = sorted(hall, key=lambda h: h.percent_vote, reverse=True)
    #hall_list = list(hall).sort(hall.year)
    return render_to_response('baseball/top_lists.html', {'hall': sorted_hall })

def hall_by_year(request):
    hall =  HallOfFame.objects.filter(inducted=True).order_by('year')
    return render_to_response('baseball/top_lists.html', {'hall': hall})


def post_season(request):
    world_series = PostSeasonSeries.objects.filter(playoff_round="WS"
                                                   ).order_by('year')
    return render_to_response('baseball/world_series.html', {'world_series': world_series })

def chart(request):
    """
    example using pygal to print a simple bar chart
    """
    import pygal

    line_chart = pygal.Bar(disable_xml_declaration=True, pretty_print=True)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(2002, 2013))
    line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    chart = line_chart.render(is_unicode=True)
    return render_to_response('baseball/chart.html', {'chart': chart})

