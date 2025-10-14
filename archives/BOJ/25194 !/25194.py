import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

dp = [False] * 7
dp[0] = True

for a in A:
    post_dp = dp.copy()
    for i in range(7):
        if dp[i]:
            post_dp[(i + a) % 7] = True
    dp = post_dp

if dp[4]:
    print('YES')
else:
    print('NO')
