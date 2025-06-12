import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * len(t) for t in triangle]
dp[0][0] = triangle[0][0]

for y in range(1, n):
    for x in range(len(dp[y])):
        if x == 0:
            dp[y][x] = triangle[y][0] + dp[y - 1][0]
        elif x == len(dp[y]) - 1:
            dp[y][x] = triangle[y][-1] + dp[y - 1][-1]
        else:
            dp[y][x] = max(triangle[y][x] + dp[y - 1][x - 1], triangle[y][x] + dp[y - 1][x])

print(max(dp[-1]))