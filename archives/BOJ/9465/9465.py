import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    dp = [[0] * n for _ in range(2)]
    
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
    else:
        dp[0][0] = stickers[0][0]
        dp[1][0] = stickers[1][0]
        
        dp[0][1] = dp[1][0] + stickers[0][1]
        dp[1][1] = dp[0][0] + stickers[1][1]
        
        for index in range(2, n):
            dp[0][index] = max(dp[1][index - 1] + stickers[0][index], dp[1][index - 2] + stickers[0][index])
            dp[1][index] = max(dp[0][index - 1] + stickers[1][index], dp[0][index - 2] + stickers[1][index])
        
        print(max(max(dp[0]), max(dp[1])))