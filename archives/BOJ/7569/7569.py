from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for n in range(N)] for h in range(H)]
visited = [[[False] * M for n in range(N)] for h in range(H)]
queue = deque()

answer_day = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append((z, y, x, 0))
                visited[z][y][x] = True

while queue:
    node_z, node_y, node_x, day = queue.popleft()
    
    deltas = [
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1)
    ]
    
    for delta in deltas:
        dz, dy, dx = delta
        z, y, x = node_z + dz, node_y + dy, node_x + dx
        
        if 0 <= z < H and 0 <= y < N and 0 <= x < M and not visited[z][y][x] and box[z][y][x] != -1:
            answer_day = max(answer_day, day + 1)
            visited[z][y][x] = True
            queue.append((z, y, x, day + 1))

def check():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 0 and not visited[z][y][x]:
                    return False
    return True

if check():
    print(answer_day)
else:
    print(-1)
                