import sys

N = int(sys.stdin.readline().strip())

def differential(C, K):
    if K != 0:
        return (C * K) * (1) ** (K - 1)
    return 0

result = 0

for i in range(N):
    C, K = map(int, sys.stdin.readline().strip().split())
    result += differential(C, K)

print(result)