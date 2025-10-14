import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

H = list(map(int, sys.stdin.readline().rstrip().split()))
A = list(map(int, sys.stdin.readline().rstrip().split()))

print(max(H) + max(A))
