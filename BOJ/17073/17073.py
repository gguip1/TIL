import sys

N, W = map(int, sys.stdin.readline().rstrip().split())

graph = {}

count = 0

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().rstrip().split())
    
    if graph.get(U) is None:
        graph[U] = [V]
    else:
        graph[U].append(V)
    
    if graph.get(V) is None:
        graph[V] = [U]
    else:
        graph[V].append(U)

for key, value in graph.items():
    if key != 1 and len(value) == 1:
        count += 1

print(f"{W / count:.10f}")