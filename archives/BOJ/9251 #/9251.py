import sys
input = sys.stdin.readline

string_1 = input().strip()
string_2 = input().strip()

dp = [[0] * (len(string_1) + 1) for _ in range(len(string_2) + 1)]

for x in range(1, len(string_1) + 1):
    for y in range(1, len(string_2) + 1):
        if string_1[x - 1] == string_2[y - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
        else:
            dp[y][x] = max(dp[y][x - 1], dp[y - 1][x])

max_value = 0

for x in range(len(string_1) + 1):
    for y in range(len(string_2) + 1):
        max_value = max(max_value, dp[y][x])

print(max_value)