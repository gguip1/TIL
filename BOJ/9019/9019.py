import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    queue = deque([(A, '')])
    visited = [False for __ in range(10001)]
    
    while queue:
        node, command = queue.popleft()
        
        if node == B:
            print(command)
            break
        
        d = (node * 2) % 10000
        s = 9999 if node == 0 else node - 1
        l = int(str(node).zfill(4)[1:] + str(node).zfill(4)[0])
        r = int(str(node).zfill(4)[-1] + str(node).zfill(4)[:-1])
        
        if not visited[d]:
            queue.append((d, command + 'D'))
            visited[d] = True
        
        if not visited[s]:
            queue.append((s, command + 'S'))
            visited[s] = True

        if not visited[l]:
            queue.append((l, command + 'L'))
            visited[l] = True
    
        if not visited[r]:
            queue.append((r, command + 'R'))
            visited[r] = True
                