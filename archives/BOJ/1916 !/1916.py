import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

paths = {}

for _ in range(M):
    S, E, V = map(int, input().split())
    
    if paths.get(S) is None:
        paths[S] = [(E, V)]
    else:
        paths[S].append((E, V))

A, B = map(int, input().split())

cities = [float('inf')] * N
cities[A - 1] = 0
queue = deque([A])
in_queue = [False] * N

while queue:
    current = queue.popleft()
    in_queue[current - 1] = False
    
    for next, value in paths.get(current, []):
        if cities[current - 1] + value < cities[next - 1]:
            cities[next - 1] = cities[current - 1] + value
            
            if not in_queue[next - 1]:
                queue.append(next)
                in_queue[next - 1] = True

print(cities[B - 1])
