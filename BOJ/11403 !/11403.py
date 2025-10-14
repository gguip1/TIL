import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

for n in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][n] and G[n][j]:
                G[i][j] = 1
                
for g in G:
    print(*g)