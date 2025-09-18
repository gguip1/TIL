import sys
input = sys.stdin.readline

N, M, K, X, Y = map(int, input().split())

costs = []

for _ in range(N):
    A, B = map(int, input().split())
    cost = A * X - B * Y
    costs.append((cost, A, B))

costs.sort()

a = 0
b = 0

for _ in range(M):
    a += costs[_][1]
    b += costs[_][2]

print((K + a) * X + (K - b) * Y)
