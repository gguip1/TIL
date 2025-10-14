import sys
input = sys.stdin.readline

N, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = (0, 0)
min_value = float('inf')

for y in range(N):
    for x in range(N):
        if board[y][x] != 1:
            value = 0
            for z in range(max(0, y - D), min(N, y + D + 1)):
                value += sum(board[z][max(0, x - D):min(N, x + D + 1)])
            if value < min_value:
                answer = (y + 1, x + 1)
                min_value = value

print(*answer)
if min_value != 0:
    print(min_value)