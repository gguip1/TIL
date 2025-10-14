import sys

input = sys.stdin.readlines

T = input()

for t in T:
    N, B, M = map(float, t.split())
    year = 0
    while N <= M:
        year += 1
        N += (N * (B / 100))
    print(year)