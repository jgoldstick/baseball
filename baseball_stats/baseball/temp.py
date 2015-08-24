a = ("at_bats", "caught_stealing", "double_plays", "doubles", "games", "games_batting",
   "hit_by_pitch", "hits", "homeruns", "intentional_walks",
   "rbi", "runs", "sac_flies", "sac_hits", " stolen_bases", "strike_outs", "triples", "walks")

b = (
"at bats", "caught stealing", "double plays", "doubles", "games", "games batting",
   "hit by pitch", "hits", "homeruns", "intentional walks",
   "rbi", "runs", "sac flies", "sac hits", " stolen bases", "strike outs", "triples", "walks"
)
b = [cat.title() for cat in b]

p1 =["balks", "batters_faced", "batting_ave_opponent", "complete_games", "double_plays",
     "earned_run_average", "earned_runs", "games", "games_finished", "games_started",
     "hit_by_pitch", "hits", "homeruns", "id", "intentional_walks", "league", "losses",
     "outs_pitched", "player", "sac_flies", "sacs_allowed", "saves", "shutouts", "stint",
     "strikeouts", "team", "walks", "wild_pitches", "wins"]

p2 =["balks", "batters_faced", "batting_ave_opponent", "complete_games", "double_plays",
     "earned_run_average", "earned_runs", "games", "games_finished", "games_started",
     "hit_by_pitch", "hits", "homeruns", "id", "intentional_walks", "league", "losses",
     "outs_pitched", "player", "sac_flies", "sacs_allowed", "saves", "shutouts", "stint",
     "strikeouts", "team", "walks", "wild_pitches", "wins"]
p2 = [cat.title() for cat in p2]
f1 = "assists, caught_stealing, double_plays, errors, games, games_started, outs_played, passed_balls, player, position, putouts, stolen_on, wild_pitches"

f1 = f1.split(", ")
f2 = f1[:]
f2 = [cat.replace("_","").title() for cat in f2]
print f1
print f2
f3 = zip(f1, f2)
print f3

pitch_catagories = zip(p1,p2)
print pitch_catagories
categories = zip(a,b)
print categories
