import sys
from copy import deepcopy

N, M = map(int, sys.stdin.readline().rstrip().split())

lab = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

def dfs(fp, sp, tp, lab):
    lab[fp[0]][fp[1]] = 1
    lab[sp[0]][sp[1]] = 1
    lab[tp[0]][tp[1]] = 1
    
    visited = [[False for _ in range(M)] for __ in range(N)]
    safety_zone = 0
    
    for y in range(N):
        for x in range(M):
            safe = True
            
            if not visited[y][x] and lab[y][x] != 1:
                count = 1
                stack = [(y, x)]
                visited[y][x] = True
                if lab[y][x] == 2:
                    safe = False
                deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                
                while stack:
                    node_y, node_x = stack.pop()
                    
                    for delta in deltas:
                        dy, dx = delta
                        
                        if 0 <= node_y + dy < N and 0 <= node_x + dx < M and not visited[node_y + dy][node_x + dx] and lab[node_y + dy][node_x + dx] != 1:
                            if lab[node_y + dy][node_x + dx] == 2:
                                safe = False
                            count += 1
                            visited[node_y + dy][node_x + dx] = True
                            stack.append((node_y + dy, node_x + dx))
                
                if safe:
                    safety_zone += count
            else:
                continue
    
    return safety_zone

answer = 0
    
for f_y in range(N):
    for f_x in range(M):
        for s_y in range(f_y, N):
            for s_x in range(f_x + 1 if f_y == s_y else 0, M):
                for t_y in range(s_y, N):
                    for t_x in range(s_x + 1 if s_y == t_y else 0, M):
                        if lab[f_y][f_x] == 0  and lab[s_y][s_x] == 0 and lab[t_y][t_x] == 0:
                            answer = max(answer, dfs((f_y, f_x), (s_y, s_x), (t_y, t_x), deepcopy(lab)))

print(answer)