import sys
input = sys.stdin.readline

OFFSET = 50
dp = [[[0 for a_index in range(101)] for b_index in range(101)] for c_index in range(101)]

dp[OFFSET + 20][OFFSET + 20][OFFSET + 20] = 1048576

for a_index in range(101):
    for b_index in range(101):
        for c_index in range(101):
            if a_index <= 0 + OFFSET or b_index <= 0 + OFFSET or c_index <= 0 + OFFSET:
                dp[a_index][b_index][c_index] = 1
            elif a_index > 20 + OFFSET or b_index > 20 + OFFSET or c_index > 20 + OFFSET:
                dp[a_index][b_index][c_index] = dp[20 + OFFSET][20 + OFFSET][20 + OFFSET]
            elif a_index < b_index and b_index < c_index:
                dp[a_index][b_index][c_index] = dp[a_index][b_index][c_index - 1] + dp[a_index][b_index - 1][c_index - 1] - dp[a_index][b_index - 1][c_index]
            else:
                dp[a_index][b_index][c_index] = dp[a_index - 1][b_index][c_index] + dp[a_index - 1][b_index - 1][c_index] + dp[a_index - 1][b_index][c_index - 1] - dp[a_index - 1][b_index - 1][c_index - 1]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = {dp[a + OFFSET][b + OFFSET][c + OFFSET]}')
