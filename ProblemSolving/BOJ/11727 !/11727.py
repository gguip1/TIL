import sys

dp = []

for i in range(1000):
    if i == 0:
        dp.append(1)
    elif i == 1:
        dp.append(3)
    else:
        dp.append((dp[i - 2] * 2 + dp[i - 1]) % 10007)

print(dp[int(sys.stdin.readline().strip()) - 1])