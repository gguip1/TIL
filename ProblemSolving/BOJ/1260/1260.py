def bfs(graph, start):
    visited = set()
    route = []
    queue = []
    
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            route.append(vertex)
            
            queue.extend(sorted(graph[vertex]))  # 작은 숫자부터 방문

    return route

def dfs(graph, start):
    visited = set()
    route = []
    stack = []
    
    stack.append(start)
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            route.append(vertex)
            visited.add(vertex)
        
            stack.extend(reversed(sorted(graph[vertex])))

    return route

import sys

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = {}
for i in range(N):
    graph[i + 1] = []

for i in range(M):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

print(*dfs(graph, V))
print(*bfs(graph, V))
