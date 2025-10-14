import sys

def dfs(y, x):
    stack = [(y, x)]
    
    while stack:
        node_y, node_x = stack.pop()
        
        if not visited[node_y][node_x] and map_[node_y][node_x] == 1:
            visited[node_y][node_x] = True
            
            if node_y < h - 1 and not visited[node_y + 1][node_x] and map_[node_y + 1][node_x] == 1:
                # visited[node_y + 1][node_x] = True
                stack.append((node_y + 1, node_x))
        
            if node_x < w - 1 and not visited[node_y][node_x + 1] and map_[node_y][node_x + 1] == 1:
                # visited[node_y][node_x + 1] = True
                stack.append((node_y, node_x + 1))
            
            if node_y > 0 and not visited[node_y - 1][node_x] and map_[node_y - 1][node_x] == 1:
                # visited[node_y - 1][node_x] = True
                stack.append((node_y - 1, node_x))
            
            if node_x > 0 and not visited[node_y][node_x - 1] and map_[node_y][node_x - 1] == 1:
                # visited[node_y][node_x - 1] = True
                stack.append((node_y, node_x - 1))
            
            if node_y > 0 and node_x > 0 and not visited[node_y - 1][node_x - 1] and map_[node_y - 1][node_x - 1] == 1:
                # visited[node_y - 1][node_x - 1] = True
                stack.append((node_y - 1, node_x - 1))
            
            if node_y < h - 1 and node_x > 0 and not visited[node_y + 1][node_x - 1] and map_[node_y + 1][node_x - 1] == 1:
                # visited[node_y + 1][node_x - 1] = True
                stack.append((node_y + 1, node_x - 1))
            
            if node_y > 0 and node_x < w - 1 and not visited[node_y - 1][node_x + 1] and map_[node_y - 1][node_x + 1] == 1:
                # visited[node_y - 1][node_x + 1] = True
                stack.append((node_y - 1, node_x + 1))
            
            if node_y < h - 1 and node_x < w - 1 and not visited[node_y + 1][node_x + 1] and map_[node_y + 1][node_x + 1] == 1:
                # visited[node_y + 1][node_x + 1] = True
                stack.append((node_y + 1, node_x + 1))
                
while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    
    map_ = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
    visited = [[False for x in range(w)] for y in range(h)]
    
    count = 0
    for j in range(h):
        for i in range(w):
            if map_[j][i] == 1 and not visited[j][i]:
                dfs(j, i)
                count += 1
    
    print(count)
