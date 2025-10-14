import sys
input = sys.stdin.readline
N, M = map(int, input().split())
seq = list(map(int, input().split()))
dp = [[-999] * N for _ in range(N)]

for idx_1 in range(N):
    for idx_2 in range(idx_1, N):
        dp[idx_2][idx_1] = max(max(dp[idx_2]), sum(seq[idx_2 - idx_1:idx_2 + 1]))
            
answer = 0

for idx_1 in range(N, -1, -1):
    for idx_2 in range(N, -1, -1):
        _range = idx_1
        _last_index = idx_2
        _cnt = 0
        
        for _ in range(M):
            cnt += 1
    
print(answer)