import sys

N = int(sys.stdin.readline().rstrip())

TP = []

for _ in range(N):
    TP.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

day = 0

for T, P in TP:
    print(T, P)
