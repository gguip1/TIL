import sys
input = sys.stdin.readline

MAX = 40

n = int(input())

recursion_dp = [0] * MAX

recursion_dp[4], recursion_dp[5] = 5, 8

for i in range(6, MAX):
    recursion_dp[i] = recursion_dp[i - 1] + recursion_dp[i - 2]

print(recursion_dp[n - 1], n - 2)