import sys
input = sys.stdin.readline

def sudoku(y=0, x=0):
    if y == 9:
        return board
    
    if x == 9:
        return sudoku(y + 1, 0)
    
    if board[y][x] != 0:
        return sudoku(y, x + 1)
    
    for value in range(1, 10):
        if value in row_used[y] or value in col_used[x] or value in box_used[y // 3][x // 3]:
            continue
        
        board[y][x] = value
        row_used[y].add(value)
        col_used[x].add(value)
        box_used[y // 3][x // 3].add(value)

        result = sudoku(y, x + 1)
        
        if result:
            return result

        board[y][x] = 0
        row_used[y].remove(value)
        col_used[x].remove(value)
        box_used[y // 3][x // 3].remove(value)

board = [list(map(int, list(input().strip()))) for _ in range(9)]

row_used = [set() for _ in range(9)]
col_used = [set() for _ in range(9)]
box_used = [[set() for _ in range(3)] for _ in range(3)]

for y in range(9):
    for x in range(9):
        value = board[y][x]
        if value != 0:
            row_used[y].add(value)
            col_used[x].add(value)
            box_used[y // 3][x // 3].add(value)

for b in sudoku():
    print(*b, sep='')
