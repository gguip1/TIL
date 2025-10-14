import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
boxes = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
day = [[0] * M for _ in range(N)]

queue = deque()

for j in range(N):
    for i in range(M):
        if boxes[j][i] == 1:
            queue.append((j, i))
            visited[j][i] = True
        if boxes[j][i] == -1:
            visited[j][i] = True

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    node_y, node_x = queue.popleft()
    
    for d in delta:
        dy, dx = d
        if 0 <= node_y + dy < N and 0 <= node_x + dx < M and not visited[node_y + dy][node_x + dx]:
            visited[node_y + dy][node_x + dx] = True
            day[node_y + dy][node_x + dx] = day[node_y][node_x] + 1
            queue.append((node_y + dy, node_x + dx))

max_value = 0

for j in range(N):
    for i in range(M):
        if not visited[j][i]:
            print(-1)
            sys.exit()
        if max_value < day[j][i]:
            max_value = day[j][i]

print(max_value)

