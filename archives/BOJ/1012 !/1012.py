import sys

T = int(sys.stdin.readline().rstrip())

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(y, x):
    global matrix, visited
    
    visited[y][x] = 1
    stack = [(y, x)]
    
    while stack:
        cy, cx = stack.pop()
        
        for i in range(4):
            newY, newX = cy + dy[i], cx + dx[i]
            if 0 <= newY < len(matrix) and 0 <= newX < len(matrix[0]):
                if matrix[newY][newX] and not visited[newY][newX]:
                    visited[newY][newX] = 1
                    stack.append((newY, newX))

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    
    matrix = [[0] * (M) for x in range(N)]
    visited = [[0] * (M) for x in range(N)]

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        matrix[Y][X] = 1    

    count = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] and not visited[i][j]:
                count += 1
                dfs(i, j)
    
    print(count)

# def dfs(y, x):
#     global matrix, visited
    
#     visited[y][x] = 1
    
#     for i in range(4):
#         newY = y + dy[i]
#         newX = x + dx[i]
#         if 0 <= newY < len(matrix) and 0 <= newX < len(matrix[0]):
#             if matrix[newY][newX] and not visited[newY][newX]:
#                 dfs(newY, newX)

# for _ in range(T):
#     M, N, K = map(int, sys.stdin.readline().rstrip().split())

#     matrix = [[0] * (M) for x in range(N)]
#     visited = [[0] * (M) for x in range(N)]
    
#     for i in range(K):
#         X, Y = map(int, sys.stdin.readline().rstrip().split())
#         matrix[Y][X] = 1    
    
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             if matrix[i][j] and not visited[i][j]:
#                 dfs(i, j)
#                 count += 1
    
#     print(count)
