from django import forms
from baseball.models import Master


years = [(y, y) for y in reversed(range(1871, 2014))]
years.insert(0, ('All', 'All'))
teams = [("All", "All"), ("ARI", "Arizona Diamondbacks"),
            ("ATL", "Atlanta Braves"),
            ("BAL", "Baltimore Orioles"),
            ("BOS", "Boston Red Sox"),
            ("CHC", "Chicago Cubs"),
            ("CHW", "Chicago White Sox"),
            ("CIN", "Cincinnati Reds"),
            ("CLE", "Cleveland Indians"),
            ("COL", "Colorado Rockies"),
            ("DET", "Detroit Tigers"),
            ("FLA", "Florida Marlins"),
            ("HOU", "Houston Astros"),
            ("KCR", "Kansas City Royals"),
            ("ANA", "Los Angeles Angels of Anaheim"),
            ("LAD", "Los Angeles Dodgers"),
            ("MIL", "Milwaukee Brewers"),
            ("MIN", "Minnesota Twins"),
            ("NYM", "New York Mets"),
            ("NYY", "New York Yankees"),
            ("OAK", "Oakland Athletics"),
            ("PHI", "Philadelphia Phillies"),
            ("PIT", "Pittsburgh Pirates"),
            ("SDP", "San Diego Padres"),
            ("SFG", "San Francisco Giants"),
            ("SEA", "Seattle Mariners"),
            ("STL", "St. Louis Cardinals"),
            ("TBD", "Tampa Bay Rays"),
            ("TEX", "Texas Rangers"),
            ("TOR", "Toronto Blue Jays"),
            ("WSN", "Washington Nationals")]
pitching_categories = [('balks', 'Balks'), ('batters_faced', 'Batters Faced'),
                        ('batting_ave_opponent', 'Batting Ave Opponent'), ('complete_games', 'Complete Games'),
                        ('double_plays', 'Double Plays'), ('earned_run_average', 'Earned Run Average'),
                        ('earned_runs', 'Earned Runs'), ('games', 'Games'), ('games_finished', 'Games Finished'),
                        ('games_started', 'Games Started'), ('hit_by_pitch', 'Hit By Pitch'), ('hits', 'Hits'),
                        ('homeruns', 'Home Runs'), ('intentional_walks', 'Intentional Walks'), ('losses', 'Losses'),
                        ('outs_pitched', 'Outs Pitched'), ('sac_flies', 'Sac Flies'), ('sacs_allowed', 'Sacs Allowed'),
                        ('saves', 'Saves'), ('shutouts', 'Shutouts'), ('strikeouts', 'Strikeouts'), ('team', 'Team'),
                        ('walks', 'Walks'), ('wild_pitches', 'Wild_Pitches'), ('wins', 'Wins')
                        ]

leagues = [("All", "All"), ("AL", "American League"), ("NL", "National League"),
            ("AA", "American Association"), ("FL", "Federal League"), ("NA", "National Association"),
            ("UA", "Union Association")]
batting_categories = [('at_bats', 'At Bats'), ('avg', 'Batting Average'), ('caught_stealing', 'Caught Stealing'), ('double_plays', 'Double Plays'),
              ('doubles', 'Doubles'), ('games', 'Games'), ('games_batting', 'Games Batting'),
              ('hit_by_pitch', 'Hit By Pitch'), ('hits', 'Hits'), ('homeruns', 'Homeruns'),
              ('intentional_walks', 'Intentional Walks'), ('rbi', 'Rbi'), ('runs', 'Runs'),
              ('sac_flies', 'Sac Flies'), ('sac_hits', 'Sac Hits'), ('stolen_bases', 'Stolen Bases'),
              ('strike_outs', 'Strike Outs'), ('triples', 'Triples'), ('walks', 'Walks')]
fielding_categories = [('assists', 'Assists'), ('caught_stealing', 'Caught Stealing'),
                       ('double_plays', 'Double Plays'), ('errors', 'Errors'), ('games', 'Games'),
                       ('games_started', 'Games Started'), ('outs_played', 'Outs Played'),
                       ('passed_balls', 'Passed Balls'), ('player', 'Player'), ('position', 'Position'),
                       ('putouts', 'Putouts'), ('stolen_on', 'Stolen On'), ('wild_pitches', 'Wild Pitches')]

all_months = [(1, "January"), (2, "February"), (3, "March"), (4, "April"), (5, "May"), (6, "June"), (7, "July"),
              (8, "August"), (9, "September"), (10, "October"), (11, "November"), (12, "December")]

countries = [(None, "All"), ("USA", "USA"), ("P.R.", "P.R"), ("Cuba", "Cuba")]

countries = Master.objects.values_list('birth_country').distinct().order_by('birth_country')
countries = [(v[0], v[0]) for v in countries]
class BirthdayForm(forms.Form):
    month = forms.ChoiceField(all_months)
    date = forms.ChoiceField(choices=((str(x), x) for x in range(1,32)))


class BattingFilterForm(forms.Form):
    category = forms.ChoiceField(batting_categories)
    year = forms.ChoiceField(years)
    team__franchise = forms.ChoiceField(teams)
    league = forms.ChoiceField(leagues)


class PitchingFilterForm(BattingFilterForm):
    category = forms.ChoiceField(pitching_categories)


class FieldingFilterForm(BattingFilterForm):
    category = forms.ChoiceField(fielding_categories)


class BirthCountryForm(forms.Form):
    year = forms.ChoiceField(years)


class PlayersForm(forms.Form):
    birth_country = forms.ChoiceField(countries)
