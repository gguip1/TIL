import sys
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(10)]

def check_horizontal(y, x) -> bool:
    if x <= 5:
        check_O = False
        count_X = 0
        for dx in range(5):
            if board[y][x + dx] == 'X':
                count_X += 1
            if board[y][x + dx] == 'O':
                check_O = True
        if not check_O and count_X >= 4:
            return True
    return False

def check_vertical(y, x) -> bool:
    if y <= 5:
        check_O = False
        count_X = 0
        for dy in range(5):
            if board[y + dy][x] == 'X':
                count_X += 1
            if board[y + dy][x] == 'O':
                check_O = True
        if not check_O and count_X >= 4:
            return True
    return False

def check_diagonal(y, x) -> bool:
    if y <= 5 and x <= 5:
        check_O = False
        count_X = 0
        for dydx in range(5):
            if board[y + dydx][x + dydx] == 'X':
                count_X += 1
            if board[y + dydx][x + dydx] == 'O':
                check_O = True
        if not check_O and count_X >= 4:
            return True
    if y >= 4 and x <= 5:
        check_O = False
        count_X = 0
        for dydx in range(5):
            if board[y - dydx][x + dydx] == 'X':
                count_X += 1
            if board[y - dydx][x + dydx] == 'O':
                check_O = True
        if not check_O and count_X >= 4:
            return True
    return False

def can_win(y, x) -> bool:
    if check_vertical(y, x) or check_horizontal(y, x) or check_diagonal(y, x):
        return True
    return False

for y in range(10):
    for x in range(10):
        if board[y][x] != 'O' and can_win(y, x):
            print(1)
            sys.exit()

print(0)