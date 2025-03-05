import sys

N = int(sys.stdin.readline())

ns = []

for i in range(N):
    ns.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    rank = 1
    for j in range(N):
        if ns[i][0] < ns[j][0] and ns[i][1] < ns[j][1]:
            rank += 1
    print(rank, end=' ')