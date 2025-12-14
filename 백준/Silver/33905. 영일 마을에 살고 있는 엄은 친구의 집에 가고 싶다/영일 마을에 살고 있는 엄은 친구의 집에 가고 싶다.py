import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = dict()

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

friends = list(map(int, input().split()))
visited = [False] * (N + 1)
visited[0] = True

for f in friends:
    visited[f - 1] = True

stack = [0]

answer = 0

while stack:
    node = stack.pop()

    neighbors = graph.get(node + 1)

    if neighbors:
        for v in neighbors:
            if not visited[v - 1]:
                stack.append(v - 1)
                visited[v - 1] = True
                answer += 1

print(answer)
