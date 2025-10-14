import sys
input = sys.stdin.readline

N, M = map(int, input().split())
soldiers = [list(input().strip()) for _ in range(M)]
    
w_power = 0
b_power = 0

w_visited = [[False] * N for _ in range(M)]

for y in range(M):
    for x in range(N):
        if not w_visited[y][x] and soldiers[y][x] == 'W':
            w_stack = [(y, x)]
            w_visited[y][x] = True
            
            headcount = 1
            
            while w_stack:
                node_y, node_x = w_stack.pop()
                
                deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dy, dx in deltas:
                    if 0 <= node_y + dy < M and 0 <= node_x + dx < N:
                        if not w_visited[node_y + dy][node_x + dx] and soldiers[node_y + dy][node_x + dx] == 'W':
                            headcount += 1
                            w_visited[node_y + dy][node_x + dx] = True
                            w_stack.append((node_y + dy, node_x + dx))
            
            w_power += headcount ** 2

b_visited = [[False] * N for _ in range(M)]

for y in range(M):
    for x in range(N):
        if not b_visited[y][x] and soldiers[y][x] == 'B':
            b_stack = [(y, x)]
            b_visited[y][x] = True
            
            headcount = 1
            
            while b_stack:
                node_y, node_x = b_stack.pop()
                
                deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dy, dx in deltas:
                    if 0 <= node_y + dy < M and 0 <= node_x + dx < N:
                        if not b_visited[node_y + dy][node_x + dx] and soldiers[node_y + dy][node_x + dx] == 'B':
                            headcount += 1
                            b_visited[node_y + dy][node_x + dx] = True
                            b_stack.append((node_y + dy, node_x + dx))
            
            b_power += headcount ** 2

print(w_power, b_power)
