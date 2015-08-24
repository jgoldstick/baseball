from django.db import models

# Create your models here.


class Master(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()
    birth_country = models.CharField(max_length=30)
    birth_state = models.CharField(max_length=30)
    birth_city = models.CharField(max_length=30)
    death_year = models.IntegerField(blank=True, null=True)
    death_month = models.IntegerField(blank=True, null=True)
    death_day = models.IntegerField(blank=True, null=True)
    death_country = models.CharField(max_length=30, blank=True)
    death_state = models.CharField(max_length=30, blank=True)
    death_city = models.CharField(max_length=30, blank=True)
    name_first = models.CharField(max_length=30)
    name_last = models.CharField(max_length=30, db_index=True)
    name_given = models.CharField(max_length=30)
    weight = models.IntegerField()
    height = models.IntegerField()
    bats = models.CharField(max_length=3)
    throws = models.CharField(max_length=3)
    debut = models.DateField(blank=True, null=True)
    final_game = models.DateField(blank=True, null=True)
    retro_id = models.CharField(max_length=30)
    bbref_id = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s %s" % (self.name_first, self.name_last)


class League(models.Model):
    short_name = models.CharField(max_length=3, primary_key=True)
    full_name = models.CharField(max_length=30)

    def __unicode__(self):
        return "%s" % self.full_name


class Salary(models.Model):
    year = models.IntegerField()
    team = models.CharField(max_length=3, db_index=True)
    league = models.CharField(max_length=3)
    player = models.ForeignKey(Master)
    salary = models.IntegerField(db_index=True)

    def __unicode__(self):
        return "%s, %d" % (self.player, self.year)

    class Meta:
        verbose_name_plural = 'salaries'


class TeamFranchise(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    active = models.BooleanField()
    na_association = models.CharField(max_length=3, blank=True)

    def __unicode__(self):
        return "%s (%s)" % (self.name, self.id)


class Team(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    year = models.IntegerField()
    league = models.CharField(max_length=4)
    team = models.CharField(max_length=4)
    franchise = models.ForeignKey(TeamFranchise)
    division = models.CharField(max_length=2, blank=True)
    rank = models.IntegerField()
    games = models.IntegerField()
    home_games = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField()
    losses = models.IntegerField()
    won_division = models.BooleanField()
    won_wildcard = models.BooleanField()
    won_pennant = models.BooleanField()
    won_world_series = models.BooleanField()
    runs = models.IntegerField()
    at_bats = models.IntegerField()
    hits = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    home_runs = models.IntegerField()
    walks = models.IntegerField()
    strike_outs = models.IntegerField()
    stolen_bases = models.IntegerField()
    caught_stealing = models.IntegerField()
    hit_by_pitch = models.IntegerField()
    sac_flies = models.IntegerField()
    opponent_runs = models.IntegerField()
    earn_runs_allowed = models.IntegerField()
    earned_run_average = models.IntegerField()
    complete_games = models.IntegerField()
    shutouts = models.IntegerField()
    saves = models.IntegerField()
    outs_pitched = models.IntegerField()
    hits_allowed = models.IntegerField()
    homeruns_allowed = models.IntegerField()
    walks_allowed = models.IntegerField()
    opposing_strikeouts = models.IntegerField()
    errors = models.IntegerField()
    double_plays = models.IntegerField()
    fielding_percentage = models.FloatField()
    team_name = models.CharField(max_length=50)
    park_name = models.CharField(max_length=50)
    attendance = models.IntegerField()
    park_factor_batting = models.FloatField()
    park_factor_pitching = models.FloatField()
    team_id_bbr = models.CharField(max_length=10)
    team_id_lahman_45 = models.CharField(max_length=10)
    team_id_retro = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s" % (self.team_name)


class Batting(models.Model):
    player = models.ForeignKey(Master)
    year = models.IntegerField()
    stint = models.IntegerField()
    # team = models.CharField(max_length=4)
    # team = models.ForeignKey(TeamFranchise)
    team = models.ForeignKey(Team)
    league = models.CharField(max_length=10)
    games = models.IntegerField()
    games_batting = models.IntegerField()
    at_bats = models.IntegerField()
    runs = models.IntegerField()
    hits = models.IntegerField()
    doubles = models.IntegerField()
    triples = models.IntegerField()
    homeruns = models.IntegerField()
    rbi = models.IntegerField()
    stolen_bases = models.IntegerField()
    caught_stealing = models.IntegerField()
    walks = models.IntegerField()
    strike_outs = models.IntegerField()
    intentional_walks = models.IntegerField()
    hit_by_pitch = models.IntegerField()
    sac_hits = models.IntegerField()
    sac_flies = models.IntegerField()
    double_plays = models.IntegerField()
    gold = models.CharField(max_length=10)

    def __unicode__(self):
        # return "%s %s %s" % (self.player.name_first, self.player.name_last, self.team)
        return "%s %s" % (self.player.name_first, self.player.name_last)

    @property
    def average(self):
        try:
            return float(self.hits)/self.at_bats
        except ZeroDivisionError:
            return 0
        except ValueError:
            return 0

    class Meta:
        verbose_name_plural = "Batting"


class Pitching(models.Model):
    player = models.ForeignKey(Master)
    year = models.IntegerField()
    stint = models.IntegerField()
    # team = models.ForeignKey(TeamFranchise)
    team = models.ForeignKey(Team)
    league = models.CharField(max_length=10)
    wins = models.IntegerField()
    losses = models.IntegerField()
    games = models.IntegerField()
    games_started = models.IntegerField()
    complete_games = models.IntegerField()
    shutouts = models.IntegerField()
    saves = models.IntegerField()
    outs_pitched = models.IntegerField()
    hits = models.IntegerField()
    earned_runs = models.IntegerField()
    homeruns = models.IntegerField()
    walks = models.IntegerField()
    strikeouts = models.IntegerField()
    batting_ave_opponent = models.FloatField()
    earned_run_average = models.FloatField()
    intentional_walks = models.IntegerField()
    wild_pitches = models.IntegerField()
    hit_by_pitch = models.IntegerField()
    balks = models.IntegerField()
    batters_faced = models.IntegerField()
    games_finished = models.IntegerField()
    sacs_allowed = models.IntegerField()
    sac_flies = models.IntegerField()
    double_plays = models.IntegerField()

    def __unicode__(self):
        return "%s %s" % (self.player.name_first, self.player.name_last)

    @property
    def innings_pitched(self):
        return self.outs_pitched/3 + self.outs_pitched % 3 * .1

    class Meta:
        verbose_name_plural = "Pitching"


class HallOfFame(models.Model):
    player = models.ForeignKey(Master)
    year = models.IntegerField(db_index=True)
    voted_by = models.CharField(max_length=30)
    ballots_cast = models.IntegerField()
    votes_needed = models.IntegerField()
    votes_received = models.IntegerField(db_index=True)
    inducted = models.BooleanField(db_index=True)
    category = models.CharField(max_length=30, db_index=True)
    needed_note = models.CharField(max_length=75, blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.player.name_first, self.player.name_last)

    @property
    def percent_vote(self):
        try:
            return float(self.votes_received)/self.ballots_cast

        except ZeroDivisionError:
            return 0

    class Meta:
        verbose_name_plural = "Hall of Famers"


class Fielding(models.Model):
    player = models.ForeignKey('Master')
    year = models.IntegerField()
    stint = models.IntegerField()
    # team = models.CharField(max_length=4)
    team = models.ForeignKey(Team)
    league = models.CharField(max_length=10)
    position = models.CharField(max_length=30)
    games = models.IntegerField()
    games_started = models.IntegerField(blank=True, null=True)
    outs_played = models.IntegerField(blank=True, null=True)
    putouts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    errors = models.IntegerField(blank=True, null=True)
    double_plays = models.IntegerField(blank=True, null=True)
    passed_balls = models.IntegerField(blank=True, null=True)
    wild_pitches = models.IntegerField(blank=True, null=True)
    stolen_on = models.IntegerField(blank=True, null=True)
    caught_stealing = models.IntegerField(blank=True, null=True)
    zone_rating = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.player.name_first, self.player.name_last)

    class Meta:
        verbose_name_plural = "Fielding"


class Manager(models.Model):
    manager = models.ForeignKey(Master)
    year = models.IntegerField()
    team = models.ForeignKey(Team)
    # team = models.CharField(max_length=4)
    league = models.CharField(max_length=10)
    in_season = models.IntegerField()
    games = models.IntegerField()
    won = models.IntegerField()
    lost = models.IntegerField()
    rank = models.IntegerField()
    player_manager = models.BooleanField()

    def __unicode__(self):
        return "%s %s" % (self.manager.name_first, self.manager.name_last)

    class Meta:
        verbose_name_plural = "Managers"


class Appearances(models.Model):
    year = models.IntegerField()
    # team = models.CharField(max_length=4)
    team = models.ForeignKey(Team)
    league = models.CharField(max_length=10)
    player = models.ForeignKey(Master)
    games = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    games_batted = models.IntegerField(null=True)
    games_defense = models.IntegerField(null=True)
    games_p = models.IntegerField(null=True)
    games_c = models.IntegerField(null=True)
    games_1b = models.IntegerField(null=True)
    games_2b = models.IntegerField(null=True)
    games_3b = models.IntegerField(null=True)
    games_ss = models.IntegerField(null=True)
    games_lf = models.IntegerField(null=True)
    games_cf = models.IntegerField(null=True)
    games_rf = models.IntegerField(null=True)
    games_of = models.IntegerField(null=True)
    games_dh = models.IntegerField(null=True)
    games_ph = models.IntegerField(null=True)
    games_pr = models.IntegerField(null=True)

    def __unicode__(self):
        return "%s %s" % (self.player.name_first, self.player.name_last)

    class Meta:
        verbose_name_plural = "Appearances"


class PostSeasonSeries(models.Model):
    """
    yearID,round,teamIDwinner,lgIDwinner,teamIDloser,lgIDloser,wins,losses,ties
    """
    year = models.IntegerField(db_index=True)
    playoff_round = models.CharField(max_length=10, db_index=True)
    team_winner = models.ForeignKey(Team, related_name="team_team_winner", db_index=True)
    league_winner = models.ForeignKey(League, related_name="league_league_winner", db_index=True)
    team_loser = models.ForeignKey(Team, related_name="team_team_loser", db_index=True)
    league_loser = models.ForeignKey(League, related_name="league_league_loser", db_index=True)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()

    def __unicode__(self):
        # return "%s (%d) - %s (%d)" % (self.team_winner.team_name, self.wins, self.team_loser.team_name, self.losses)
        return "%d (%d) - (%d)" % (self.year, self.wins, self.losses)

    class Meta:
        verbose_name_plural = "Post Season Series"
