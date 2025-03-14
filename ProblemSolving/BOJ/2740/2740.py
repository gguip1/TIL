import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().rstrip().split())
B = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

matrix = []

for i in range(N):
    element = []
    for j in range(K):
        ele = 0
        for z in range(M):
            ele += A[i][z] * B[z][j]
        element.append(ele)
    matrix.append(element)

for m in matrix:
    for element in m:
        print(element, end=' ')
    print()