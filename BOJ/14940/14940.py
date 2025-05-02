import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
distance = [[0] * m for _ in range(n)]

for y in range(n):
    for x in range(m):
        if board[y][x] == 2:
            target_coordinate = (y, x)

target_y, target_x = target_coordinate

queue = [(target_y, target_x)]
visited[target_y][target_x] = True

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    node_y, node_x = queue.pop(0)
    
    for d in delta:
        dy, dx = d
        
        y = node_y + dy
        x = node_x + dx
        
        if 0 <= y < n and 0 <= x < m and not visited[y][x]:
            if board[y][x] == 1:
                queue.append((y, x))
                visited[y][x] = True
                distance[y][x] = distance[node_y][node_x] + 1

for y in range(n):
    for x in range(m):
        if visited[y][x] or board[y][x] == 0:
            print(distance[y][x], end=' ')
        else:
            print(-1, end=' ')
    print()
    

