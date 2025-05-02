import sys

N = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())

dp = [[0 for x in range(len(nums))] for x in range(len(nums))]

for y in range(len(nums)):
    for x in range(len(nums)):
        if x - y >= 0:
            dp[x][x - y] = 1

print(dp)