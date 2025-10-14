import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    
    if graph.get(u) is None:
        graph[u] = [v]
    else:
        graph[u].append(v)
    
    if graph.get(v) is None:
        graph[v] = [u]
    else:
        graph[v].append(u)

stack = [R]
visited = [False] * (N + 1)

path = [0] * (N + 1)
sequence = 1

while stack:
    node = stack.pop()
    
    if visited[node]:
        continue
    else:
        visited[node] = True
        path[node] = sequence
        sequence += 1
    
    if graph.get(node):
        for _ in sorted(graph[node], reverse=True):
            if not visited[_]:
                stack.append(_)

print(*path[1:], sep='\n')
