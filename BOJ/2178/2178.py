import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

maze = [list(map(int, str(sys.stdin.readline().rstrip()))) for _ in range(N)]

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

visited = [[False for m in range(M)] for n in range(N)]
distance = [[0]*M for _ in range(N)]

def bfs(y, x):
    queue = [(y, x)]
    visited[y][x] = True
    distance[y][x] = 1
    
    while queue:
        node_y, node_x = queue.pop(0)
        
        for d in delta:
            dy, dx = d
            if 0 <= node_y + dy < N and 0 <= node_x + dx < M:
                if not visited[node_y + dy][node_x + dx] and maze[node_y + dy][node_x + dx] == 1:
                    visited[node_y + dy][node_x + dx] = True
                    distance[node_y + dy][node_x + dx] = distance[node_y][node_x] + 1
                    queue.append((node_y + dy, node_x + dx))

bfs(0, 0)
print(distance[N - 1][M - 1])