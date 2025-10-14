import sys
input = sys.stdin.readline

dp = [0] * 30
dp[0] = 1
dp[1] = 2

for i in range(1, 30):
    dp[i] = dp[i - 1]

while True:
    N = int(input())
    
    if N == 0:
        break
    
    print(dp[N - 1])