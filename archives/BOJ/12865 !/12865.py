import sys

input = sys.stdin.readline
N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * K for _ in range(N)]


for index_K in range(K):
    for index_N, item in enumerate(items):
        W, V = item
        
        if index_N == 0 and (W - 1) <= index_K:
            dp[index_N][index_K] = V
        elif (W - 1) <= index_K:
            dp[index_N][index_K] = dp[index_N - 1][index_K] + V
        
for d in dp:
    print(d)