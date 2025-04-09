import sys

graph = {}
stack = []
visited = []

N, M = map(int, sys.stdin.readline().rstrip().split())
for _ in range(N):
    graph[_] = []
    visited.append(False)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

def dfs(start):
    stack.append(start)
    visited[start] = True
    
    while stack:
        node = stack.pop()
        
        for neighbor in reversed(graph[node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

result = 0
for node in range(N):
    if not visited[node]:
        dfs(node)
        result += 1

print(result)