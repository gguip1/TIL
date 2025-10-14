import sys
input = sys.stdin.readline

N = int(input())

costs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for index in range(N):
    if index == 0:
        dp[index][0], dp[index][1], dp[index][2] = costs[index][0], costs[index][1], costs[index][2]
    else:
        dp[index][0] = min(dp[index - 1][1], dp[index - 1][2]) + costs[index][0]
        dp[index][1] = min(dp[index - 1][0], dp[index - 1][2]) + costs[index][1]
        dp[index][2] = min(dp[index - 1][0], dp[index - 1][1]) + costs[index][2]
        # dp[index][0] = min(dp[index - 2][1], dp[index - 2][2]) + min(costs[index - 1][0], costs[index - 1][1], costs[index - 1][2]) + costs[index][0]
        # dp[index][1] = min(dp[index - 2][0], dp[index - 2][2]) + min(costs[index - 1][0], costs[index - 1][1], costs[index - 1][2]) + costs[index][1]
        # dp[index][2] = min(dp[index - 2][0], dp[index - 2][1]) + min(costs[index - 1][0], costs[index - 1][1], costs[index - 1][2]) + costs[index][2]

print(min(dp[-1][0], dp[-1][1], dp[-1][2]))