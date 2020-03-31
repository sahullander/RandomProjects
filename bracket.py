import random

class Job:
    def __init__(job, name, seed):
        job.name = name
        job.seed = seed

locations = []

locations.append( Job('PoppySeedChicken', 0))
locations.append( Job('ChickenEnchilladas', 0))
locations.append( Job('SpeghettiMeatballs', 0))
locations.append( Job('ChickenRiceBake', 0))
locations.append( Job('Burgers', 0))

seeded = []

seed = [1, 2, 3, 4, 5]
random.shuffle(seed)
random.shuffle(seed)
random.shuffle(seed)
random.shuffle(seed)
random.shuffle(seed)

g1teams = []
g2teams = []
g3teams = []
g4teams = []
# losers bracket games
g5teams = []
g6teams = []
g7teams = []
# championship
g8teams = []
g9teams = []

while seed:
    location = random.choice(locations)
    if location.name not in seeded:
        seeded.append(location.name)
        randSeed = seed.pop()
        setattr(location, 'seed', randSeed)
        if randSeed == 4 or randSeed == 5:
            g1teams.append(location)
        elif randSeed == 2 or randSeed == 3:
            g2teams.append(location)
        else: g3teams.append(location)
    else: pass

games = [g1teams, g2teams, g3teams, g4teams, g5teams, g6teams, g7teams, g8teams]

coin = [0,1]
gamenum = 1

print("\nHigher seed = heads. Lower seed = tails.")
for game in games:
    if gamenum == 1:
        print("\n       Winners Bracket Games")
    elif gamenum == 5:
        print("\n       Losers Bracket Games")
    elif gamenum == 8 or gamenum == 9:
        print("\n       Championship Game!")
    if gamenum is not 8:
        game.sort(key=lambda x: x.seed)

    print("\nGame " + str(gamenum) + " matchup is between " + game[0].name + " (" + str(game[0].seed) + ") and " + game[1].name + " (" + str(game[1].seed) + ")")
    heads = 0
    tails = 0

    while heads < 2 and tails < 2:
        flip = random.choice(coin)
        if flip == 0:
            tails = tails + 1
        else:
            heads = heads + 1

    if heads > tails:
        result = 0
    else: result = 1

    if result == 0:
        winner = game[0]
        loser = game[1]
    else:
        winner = game[1]
        loser = game[0]

    print("heads count: " + str(heads) + "  tails count: " + str(tails))
    print("Winner: " + winner.name)

    if gamenum == 1:
        g3teams.append(winner)
        g5teams.append(loser)
    elif gamenum == 2:
        g4teams.append(winner)
        g5teams.append(loser)
    elif gamenum == 3:
        g4teams.append(winner)
        g6teams.append(loser)
    elif gamenum == 4:
        g8teams.append(winner)
        g7teams.append(loser)
    elif gamenum == 5:
        g6teams.append(winner)
    elif gamenum == 6:
        g7teams.append(winner)
    elif gamenum == 7:
        g8teams.append(winner)
    elif gamenum == 8 and winner == game[1]:
        print("Loser won game 1! Initiating game 2.")
        g9teams.append(winner)
        g9teams.append(loser)
        games.append(g9teams)

    gamenum = gamenum + 1
