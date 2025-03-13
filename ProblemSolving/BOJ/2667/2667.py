import sys

N = int(sys.stdin.readline().rstrip())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

matrix = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j, value in enumerate(list(sys.stdin.readline().rstrip())):
        matrix[i][j] = int(value)

def dfs(y, x, num):
    global matrix, visited
    
    stack = []
    visited[y][x] = num
    stack.append((y, x))
    
    while stack:
        cy, cx = stack.pop()
        
        for i in range(4):
            newY = cy + dy[i]
            newX = cx + dx[i]
            
            if 0 <= newY < len(matrix) and 0 <= newX < len(matrix[0]):
                if matrix[newY][newX] and not visited[newY][newX]:
                    visited[newY][newX] = num
                    stack.append((newY, newX))

num = 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] and not visited[i][j]:
            num += 1
            dfs(i, j, num)


print(num)
houses = [0] * (N ** 2)

for i in range(N):
    for j in range(N):
        if visited[i][j]:
            houses[visited[i][j]] += 1

houses.sort()

for h in houses:
    if h:
        print(h)