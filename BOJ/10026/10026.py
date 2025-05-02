import sys

N = int(sys.stdin.readline().rstrip())

img = []
visited = []

for _ in range(N):
    img.append(list(sys.stdin.readline().rstrip()))
    visited.append([False for _ in range(N)])

def dfs(y, x, color):
    stack = [(y, x)]
    
    while stack:
        node_y, node_x = stack.pop()
        
        if not visited[node_y][node_x]:
            visited[node_y][node_x] = True
            if node_y < N - 1 and img[node_y + 1][node_x] in color:
                stack.append((node_y + 1, node_x))
            if node_x < N - 1 and img[node_y][node_x + 1] in color:
                stack.append((node_y, node_x + 1))
            if node_y > 0 and img[node_y - 1][node_x] in color:
                stack.append((node_y - 1, node_x))
            if node_x > 0 and img[node_y][node_x - 1] in color:
                stack.append((node_y, node_x - 1))

result = 0

for i in range(N):
    for j in range(N):
        if not visited[j][i]:
            dfs(j, i, [img[j][i]])
            result += 1

result_rg = 0
visited = [[False for __ in range(N)]  for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[j][i]:
            if img[j][i] in ['R', 'G']:
                dfs(j, i, ['R', 'G'])
                result_rg += 1
            else:
                dfs(j, i, [img[j][i]])
                result_rg += 1

print(result, result_rg)