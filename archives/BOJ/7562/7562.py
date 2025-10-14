import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

deltas = [(-1, -2),(-2, -1),(-2, 1),(-1, 2),(2, 1),(1, 2),(1, -2),(2, -1)]

for _ in range(T):
    l = int(input())
    s_y, s_x = map(int, input().split())
    t_y, t_x = map(int, input().split())

    board = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]
    queue = deque()
    
    visited[s_y][s_x] = True
    queue.append((s_y, s_x, 0))
    
    while queue:
        node_y, node_x, cnt = queue.popleft()
        
        if node_y == t_y and node_x == t_x:
            print(cnt)
            break
        
        for delta in deltas:
            dy, dx = delta
            y, x = node_y + dy, node_x + dx

            if 0 <= y < l and 0 <= x < l and not visited[y][x]:
                visited[y][x] = True
                queue.append((y, x, cnt + 1))