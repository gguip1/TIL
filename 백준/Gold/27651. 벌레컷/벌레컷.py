import sys
input = sys.stdin.readline

from bisect import bisect_left

N = int(input())
As = list(map(int, input().split()))

prefixSum = []

for idx in range(N):
    if idx == 0:
        prefixSum.append(As[idx])
    else:
        prefixSum.append(prefixSum[idx - 1] + As[idx])

answer = 0

for Y in range(N - 2, - 1, - 1):
    limit = min(prefixSum[N - 1] - prefixSum[Y], prefixSum[Y] - (prefixSum[N - 1] - prefixSum[Y]))    
    answer += bisect_left(prefixSum, limit)

print(answer)