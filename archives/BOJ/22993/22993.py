import sys
input = sys.stdin.readline

N = int(input())
players = list(map(int, input().split()))

for player in sorted(players[1:]):
    if players[0] > player:
        players[0] += player
    else:
        print('No')
        exit()

print('Yes')
