import sys
input = sys.stdin.readline

N = int(input())

answer = 0

columns = set()
diag1 = set()
diag2 = set()

def solve(y):
    global answer
    if y == N:
        answer += 1
        return
    
    for x in range(N):
        if x in columns or (y + x) in diag1 or (y - x) in diag2:
            continue
        
        columns.add(x)
        diag1.add(y + x)
        diag2.add(y - x)
        
        solve(y + 1)
        
        columns.remove(x)
        diag1.remove(y + x)
        diag2.remove(y - x)

solve(0)

print(answer)

# import sys
# input = sys.stdin.readline

# N = int(input())

# answer = 0
# board = [[False] * N for _ in range(N)]

# def is_valid(y, x):
#     for _y in range(y):
#         if board[_y][x]:
#             return False
    
#     _y, _x = y - 1, x - 1
#     while _y >= 0 and _x >= 0:
#         if board[_y][_x]:
#             return False
#         _y -= 1
#         _x -= 1
    
#     _y, _x = y - 1, x + 1
#     while _y >= 0 and _x < N:
#         if board[_y][_x]:
#             return False
#         _y -= 1
#         _x += 1
    
#     return True

# def solve(y):
#     global answer
#     if y == N:
#         answer += 1
#         return
    
#     for x in range(N):
#         if is_valid(y, x):
#             board[y][x] = True
#             solve(y + 1)
#             board[y][x] = False

# solve(0)

# print(answer)
