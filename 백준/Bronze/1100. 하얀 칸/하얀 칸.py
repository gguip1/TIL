import sys
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(8)]

answer = 0

for y in range(8):
    for x in range(8):
        if y % 2 == 0 and x % 2 == 0:
            if board[y][x] == 'F':
                answer += 1
        elif y % 2 == 1 and x % 2 == 1:
            if board[y][x] == 'F':
                answer += 1

print(answer)
