import sys

N = int(sys.stdin.readline().strip())
stairs = [0] + [int(sys.stdin.readline().strip()) for x in range(N)]

dp = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        dp[i] = stairs[i]
    elif i == 2:
        dp[i] = dp[i - 1] + stairs[i]
    else:
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp)
print(dp[N])