import sys

T = int(sys.stdin.readline().strip())

dp = [0] * 10

for i in range(len(dp)):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 2
    elif i == 2:
        dp[i] = 4
    else:
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n - 1])