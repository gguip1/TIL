import sys
input = sys.stdin.readline

dp = [0]
n = int(input())

for i in range(1, n + 1):
    min_count = 4
    j = max(1, int(i / 232))
    while (j ** 2) <= i:
        min_count = min(min_count, dp[i - j ** 2] + 1)
        j += 1
    dp.append(min_count)

print(dp[n])
