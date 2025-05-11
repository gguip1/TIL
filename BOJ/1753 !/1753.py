import sys
import heapq

V, E = map(int, sys.stdin.readline().rstrip().split())
K = int(sys.stdin.readline().rstrip())

shortest = [float('inf')] * (V)
graph = {}

for _ in range(V):
    graph[_ + 1] = []

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v, w))

heap = [(0, K)]
shortest[K - 1] = 0

while heap:
    dist, node = heapq.heappop(heap)
    
    if shortest[node - 1] < dist:
        continue
    
    for v, w in graph[node]:
        new_dist = dist + w
        if new_dist < shortest[v - 1]:
            shortest[v - 1] = new_dist
            heapq.heappush(heap, (new_dist, v))

for i in range(len(shortest)):
    if shortest[i] == float('inf'):
        print('INF')
    else:
        print(shortest[i])