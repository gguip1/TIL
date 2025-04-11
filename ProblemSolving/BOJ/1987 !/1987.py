import sys

R, C = map(int, sys.stdin.readline().rstrip().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited_alphas = [False] * 26
record = [[[]  for _ in range(C)] for _ in range(R)]

stack = [(0, 0)]
record[0][0].append(board[0][0])

result = 0

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(y, x, path):
    global result
    result = max(result, len(path))
    
    for dy, dx in delta:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx] not in path:
                dfs(ny, nx, path + board[ny][nx])

dfs(0, 0, board[0][0])
print(result)