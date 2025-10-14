import sys

N = int(sys.stdin.readline().strip())

players = [list(map(int, sys.stdin.readline().strip().split())) for x in range(N)]
    
games = [[], [], []]

for player in players:
    games[0].append(player[0])
    games[1].append(player[1])
    games[2].append(player[2])

scores = [0 for x in range(N)]

for index, player in enumerate(players):
    score = 0
    
    for i, game in enumerate(games):
        
        length = 0
        for g in game:
            if g == player[i]:
                length += 1
        
        if length == 1:
            score += player[i]
    
    scores[index] = score

for score in scores:
    print(score)