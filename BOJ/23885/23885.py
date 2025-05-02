import sys

N, M = map(int, sys.stdin.readline().split())
sx, sy = map(int, sys.stdin.readline().split())
ex, ey = map(int, sys.stdin.readline().split())

if N == 1 or M == 1:
    if sx == ex and sy == ey:
        print('YES')
    else:
        print('NO')
else:
    if (sx + sy) % 2 == (ex + ey) % 2:
        print('YES')
    else:
        print('NO')
