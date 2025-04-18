import sys

M, N, K = map(int, sys.stdin.readline().rstrip().split())

matrix = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    
    for y in range(y1, y2):
        for x in range(x1, x2):
            # matrix[M - 1 - y][x] = 1
            matrix[y][x] = 1

result = []

for y in range(M):
    for x in range(N):
        if matrix[y][x] != 1 and not visited[y][x]:
            
            stack = []
            visited[y][x] = True
            stack.append((y, x))

            extent = 1
            while stack:
                node_y, node_x = stack.pop()
                
                if node_y - 1 >= 0 and matrix[node_y - 1][node_x] != 1 and not visited[node_y - 1][node_x]:
                    stack.append((node_y - 1, node_x))
                    visited[node_y - 1][node_x] = True
                    extent += 1
                
                if node_y + 1 < M and matrix[node_y + 1][node_x] != 1 and not visited[node_y + 1][node_x]:
                    stack.append((node_y + 1, node_x))
                    visited[node_y + 1][node_x] = True
                    extent += 1
                
                if node_x - 1 >= 0 and matrix[node_y][node_x - 1] != 1 and not visited[node_y][node_x - 1]:
                    stack.append((node_y, node_x - 1))
                    visited[node_y][node_x - 1] = True
                    extent += 1
                
                if node_x + 1 < N and matrix[node_y][node_x + 1] != 1 and not visited[node_y][node_x + 1]:
                    stack.append((node_y, node_x + 1))
                    visited[node_y][node_x + 1] = True
                    extent += 1
                
            result.append(extent)

print(len(result))
print(*sorted(result))