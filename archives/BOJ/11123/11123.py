import sys
input = sys.stdin.readline

T = int(input().strip())

def dfs(y, x, visited, H, W, sheep_ranch):
    stack = [(y, x)]
    
    while stack:
        node_y, node_x = stack.pop()
        visited[node_y][node_x] = True
        
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for delta in deltas:
            dy, dx = delta
            
            if 0 <= node_y + dy < H and 0 <= node_x + dx < W and not visited[node_y + dy][node_x + dx] and sheep_ranch[node_y + dy][node_x + dx] == '#':
                stack.append((node_y + dy, node_x + dx))
    
    return visited

for _ in range(T):
    H, W = map(int, input().split())

    cnt = 0
    sheep_ranch = [list(input().strip()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    
    for h in range(H):
        for w in range(W):
            if not visited[h][w] and sheep_ranch[h][w] == '#':
                visited = dfs(h, w, visited, H, W, sheep_ranch)
                cnt += 1
    
    print(cnt)
    