import sys

W, H = map(int, sys.stdin.readline().rstrip().split())
building = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(1, H + 1):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, W + 1):
        building[i][j] = row[j - 1]
visited = [[False] * (W + 2) for _ in range(H + 2)]
answer = 0

stack = [(0, 0)]
visited[0][0] = True

even_case = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
odd_case = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]

while stack:
    node_y, node_x = stack.pop()
    
    if node_y % 2 == 1:
        for case in even_case:
            dy, dx = case
            y, x = node_y + dy, node_x + dx
            
            if 0 <= y < H + 2 and 0 <= x < W + 2:
                if building[y][x] == 1:
                    answer += 1
                
                if not visited[y][x] and building[y][x] == 0:
                    visited[y][x] = True
                    stack.append((y, x))
    else:
        for case in odd_case:
            dy, dx = case
            y, x = node_y + dy, node_x + dx
            
            if 0 <= y < H + 2 and 0 <= x < W + 2:
                if building[y][x] == 1:
                    answer += 1
                
                if not visited[y][x] and building[y][x] == 0:
                    visited[y][x] = True
                    stack.append((y, x))

print(answer)