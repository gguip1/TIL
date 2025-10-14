import sys
input = sys.stdin.readline
N = int(input())

MAX = 90
dp = [0] * MAX

for i in range(MAX):
    if i == 0 or i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]
        
    
print(dp[N - 1])
