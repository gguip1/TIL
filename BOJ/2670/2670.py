import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * N

for idx in range(N):
    num = float(input())
    if idx == 0:
        dp[idx] = num
    else:
        if dp[idx - 1] * num > num:
            dp[idx] = dp[idx - 1] * num
        else:
            dp[idx] = num

print("{:.3f}".format(max(dp)))