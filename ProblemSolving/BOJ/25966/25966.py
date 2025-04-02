import sys
import copy

N, M, q = map(int, sys.stdin.readline().rstrip().split())

matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for _ in range(q):
    query = list(sys.stdin.readline().rstrip().split())
    
    if query[0] == '0':
        i, j, k = map(int, query[1:])
        matrix[i][j] = k
    elif query[0] == '1':
        i, j = map(int, query[1:])
        matrix[i], matrix[j] = matrix[j], matrix[i]

for y in matrix:
    print(*y)