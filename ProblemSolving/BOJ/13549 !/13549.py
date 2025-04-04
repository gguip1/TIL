import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

def bfs(N, K):
    visited = [False] * 100001
    queue = deque()
    
    visited[N] = True
    queue.append([N, 0])
    
    while queue:
        pos, sec = queue.popleft()
        
        if pos == K:
            print(sec)
            return
        
        if 0 <= pos * 2 <= 100000 and not visited[pos * 2]:
            visited[pos * 2] = True
            queue.appendleft((pos * 2, sec))
        
        for walk_pos in [pos - 1, pos + 1]:
            if 0 <= walk_pos <= 100000 and not visited[walk_pos]:
                visited[walk_pos] = True
                queue.append((walk_pos, sec + 1))
    
bfs(N, K)