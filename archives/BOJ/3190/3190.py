import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

board = [[0] * N for _ in range(N)]

for _ in range(K):
    column, row = map(int, sys.stdin.readline().rstrip().split())
    board[column - 1][row - 1] = 1

snake_position = [(0, 0)]
snake_dir = 90
game_time = 0
L = int(sys.stdin.readline().rstrip())

def is_board_out(x, y) -> bool:
    if 0 <= x < N and 0 <= y < N:
        return False
    else:
        return True

def is_snake_body(x, y) -> bool:
    if board[y][x] == 2:
        return True
    else:
        return False

def is_apple(x, y) -> bool:
    if board[y][x] == 1:
        return True
    else:
        return False

def is_game_over(move_count = 100) -> bool:
    global game_time
    for _ in range(move_count):
        snake_x, snake_y = snake_position[-1]
        if snake_dir % 360 ==  0 and not is_board_out(snake_x, snake_y - 1) and not is_snake_body(snake_x, snake_y - 1):
            if is_apple(snake_x, snake_y - 1):
                board[snake_y - 1][snake_x] = 2
                snake_position.append((snake_x, snake_y - 1))
            else:
                snake_tail_x, snake_tail_y = snake_position.pop(0)
                board[snake_tail_y][snake_tail_x] = 0
                board[snake_y - 1][snake_x] = 2
                snake_position.append((snake_x, snake_y - 1))
        elif snake_dir % 360 == 90 and not is_board_out(snake_x + 1, snake_y) and not is_snake_body(snake_x + 1, snake_y):
            if is_apple(snake_x + 1, snake_y):
                board[snake_y][snake_x + 1] = 2
                snake_position.append((snake_x + 1, snake_y))
            else:
                snake_tail_x, snake_tail_y = snake_position.pop(0)
                board[snake_tail_y][snake_tail_x] = 0
                board[snake_y][snake_x + 1] = 2
                snake_position.append((snake_x + 1, snake_y))
        elif snake_dir % 360 == 180 and not is_board_out(snake_x, snake_y + 1) and not is_snake_body(snake_x, snake_y + 1):
            if is_apple(snake_x, snake_y + 1):
                board[snake_y + 1][snake_x] = 2
                snake_position.append((snake_x, snake_y + 1))
            else:
                snake_tail_x, snake_tail_y = snake_position.pop(0)
                board[snake_tail_y][snake_tail_x] = 0
                board[snake_y + 1][snake_x] = 2
                snake_position.append((snake_x, snake_y + 1))
        elif snake_dir % 360 == 270 and not is_board_out(snake_x - 1, snake_y) and not is_snake_body(snake_x - 1, snake_y):
            if is_apple(snake_x - 1, snake_y):
                board[snake_y][snake_x - 1] = 2
                snake_position.append((snake_x - 1, snake_y))
            else:
                snake_tail_x, snake_tail_y = snake_position.pop(0)
                board[snake_tail_y][snake_tail_x] = 0
                board[snake_y][snake_x - 1] = 2
                snake_position.append((snake_x - 1, snake_y))
        else:
            return True
        
        game_time += 1

    return False

Q = []

for _ in range(L):
    X, C = sys.stdin.readline().rstrip().split()
    X = int(X)
    
    Q.append((X, C))

for X, C in Q:
    if is_game_over(X - game_time):
        break
    
    if C == 'L':
        snake_dir -= 90
        if snake_dir < 0:
            snake_dir += 360
    elif C == 'D':
        snake_dir += 90

while not is_game_over():
    continue

print(game_time + 1)
