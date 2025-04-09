import sys

N = int(sys.stdin.readline().rstrip())
_map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# visited = [[False for _ in range(N)] for __ in range(N)]

def dfs(y, x, rain):
    stack = [(y, x)]
    
    while stack:
        node_y, node_x = stack.pop()

        if _map[node_y][node_x] > rain:
            if not visited[node_y][node_x]:
                visited[node_y][node_x] = True
            
            if node_y < N - 1 and not visited[node_y + 1][node_x]:
                visited[node_y + 1][node_x] = True
                stack.append((node_y + 1, node_x))
            
            if node_x < N - 1 and not visited[node_y][node_x + 1]:
                visited[node_y][node_x + 1] = True
                stack.append((node_y, node_x + 1))
            
            if node_y > 0 and not visited[node_y - 1][node_x]:
                visited[node_y - 1][node_x] = True
                stack.append((node_y - 1, node_x))
            
            if node_x > 0 and not visited[node_y][node_x - 1]:
                visited[node_y][node_x - 1] = True
                stack.append((node_y, node_x - 1))

max_count = 0
for rain in range(0, 101):
    visited = [[False for _ in range(N)] for __ in range(N)]
    count = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and _map[y][x] > rain:
                dfs(y, x, rain)
                count += 1
    if count > max_count:
        max_count = count

print(max_count)