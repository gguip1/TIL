import sys
input = sys.stdin.readline
INF = int(10e9)

n = int(input())
m = int(input())

matrix = [[INF] * n for _ in range(n)]

for idx in range(n):
    matrix[idx][idx] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a - 1][b - 1] = min(matrix[a - 1][b - 1], c)
    
for k in range(n):
    for a in range(n):
        for b in range(n):
            matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

for y in range(n):
    for x in range(n):
        if matrix[y][x] == INF:
            print(0, end=' ')
        else:
            print(matrix[y][x],end=' ')
    print()
