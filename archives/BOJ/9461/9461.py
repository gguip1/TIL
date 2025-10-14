import sys
input = sys.stdin.readline

T = int(input())

dp = [1, 1, 1]

for _ in range(3, 100):
    dp.append(dp[_ - 3] + dp[_ - 2])

for _ in range(T):
    print(dp[int(input()) - 1])
