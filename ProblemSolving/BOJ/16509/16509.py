import sys

R1, C1 = map(int, sys.stdin.readline().rstrip().split())
R2, C2 = map(int, sys.stdin.readline().rstrip().split())

board = [[0] * 9 for r in range(10)]
visited = [[False for c in range(9)] for r in range(10)]
count = [[0] * 9 for r in range(10)]

delta = [(-1, 0, -2, -2, -2, 2), (1, 0, 2, 2, -2, 2), (0, -1, -2, 2, -2, -2), (0, 1, -2, 2, 2, 2)]

def bfs():
    queue = [(R1, C1)]
    visited[R1][C1] = True
    board[R2][C2] = 1
    
    while queue:
        r, c = queue.pop(0)
        
        for d in delta:
            dy, dx, ay, by, ax, bx = d
            
            t1_y, t1_x = (r + dy + ay, c + dx + ax)
            t2_y, t2_x = (r + dy + by, c + dx + bx)
            
            if 0 <= t1_y < 10 and 0 <= t1_x < 9:
                if board[r + dy][c + dx] == 0 and board[r + dy + ay // 2][c + dx + ax // 2] == 0:
                    if not visited[t1_y][t1_x]:
                        visited[t1_y][t1_x] = True
                        count[t1_y][t1_x] = count[r][c] + 1
                        queue.append((t1_y, t1_x))
            
            if 0 <= t2_y < 10 and 0 <= t2_x < 9:
                if board[r + dy][c + dx] == 0 and board[r + dy + by // 2][c + dx + bx // 2] == 0:
                    if not visited[t2_y][t2_x]:
                        visited[t2_y][t2_x] = True
                        count[t2_y][t2_x] = count[r][c] + 1
                        queue.append((t2_y, t2_x))

bfs()
print(count[R2][C2])
