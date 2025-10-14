import sys

N = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))

result = 0

for i in range(N):
    if A[i] > B[i]:
        result += abs(A[i] - B[i])

print(result)
