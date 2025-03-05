import sys

N, K = map(int, sys.stdin.readline().strip().split())

A = [int(sys.stdin.readline().strip()) for x in range(N)]

coin = 0

for i in range(N - 1, -1, -1):
    if K // A[i] > 0:
        coin += (K // A[i])
        K -= A[i] * (K // A[i])

print(coin)    
