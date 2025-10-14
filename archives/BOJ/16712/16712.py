import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

participants = list(map(int, sys.stdin.readline().rstrip().split()))
exceptRanks = list(map(int, sys.stdin.readline().rstrip().split()))

game = 0
while game < len(exceptRanks):
    ranks = sorted(participants[:M])
    # print('Before : ', participants)
    participants.remove(ranks[exceptRanks[game] - 1])
    # print('After : ', participants)
    
    game += 1

print(*sorted(participants))
