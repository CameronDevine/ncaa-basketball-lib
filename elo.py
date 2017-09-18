import ncaa

games = ncaa.download(start = "11/4/16", end = "11/10/16")

elo_init = 1200
elo_k = 20

def elo_recalc(scores):
	# Add Elo code here
	return [scores[0] + 10, scores[1] - 10]

teams = {}

for game in games:
	for team in game:
		if team not in teams:
			teams[team] = elo_init

for game in games:
	new_scores = elo_recalc([teams[game[0]], teams[game[1]]])
	teams[game[0]] = new_scores[0]
	teams[game[1]] = new_scores[1]

print teams
