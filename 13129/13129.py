import sys

A, B, N = map(int, sys.stdin.readline().strip().split())

for i in range(1, N + 1):
    print((A + B) * i + A * (N - i))
