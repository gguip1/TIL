import sys

N, M = map(int, sys.stdin.readline().split())

BOARD = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def check(board):
    resultSW = 0
    for y in range(8):
        for x in range(8):
            if (y + x) % 2 == 0:
                if board[y][x] != 'W':
                    resultSW += 1
            else:
                if board[y][x] != 'B':
                    resultSW += 1
    
    resultSB = 0
    for y in range(8):
        for x in range(8):
            if (y + x) % 2 == 0:
                if board[y][x] != 'B':
                    resultSB += 1
            else:
                if board[y][x] != 'W':
                    resultSB += 1
    
    return resultSW if resultSW < resultSB else resultSB

result = None

for y in range(N - 8 + 1):
    for x in range(M - 8 + 1):
        sub_board = [row[x:x + 8] for row in BOARD[y:y + 8]]
        check_value = check(sub_board)
        if result is None or result > check_value:
            result = check_value

print(result)
