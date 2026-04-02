import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

for t in range(1, K + 1):
    a = 1
    for n in range(t):
        a *= (N - M - n) / (N - n)
    print(f"{1 - a:.10f}")