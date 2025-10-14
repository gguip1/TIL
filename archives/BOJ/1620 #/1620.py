import sys

N, M = map(int, input().split())

pokedex_key = {}
pokedex_value = {}

nums = [str(x + 1) for x in range(N)]

for i in range(N):
    Q = sys.stdin.readline().strip()
    pokedex_key[i + 1] = Q
    pokedex_value[Q] = str(i + 1)

for i in range(M):
    Q = sys.stdin.readline().strip()
    try:
        Q = int(Q)
        print(pokedex_key[Q])
    except:
        print(pokedex_value[Q])
