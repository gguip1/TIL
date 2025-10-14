import sys

n = int(sys.stdin.readline().rstrip())
target_1, target_2 = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())

graph = {
    
}

for i in range(n):
    graph[i + 1] = []

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    
    graph[x].append(y)
    graph[y].append(x)

stack = []
visited = [False] * n
family = [0] * n

stack.append(target_1)
family[target_1 - 1] += 1

while stack:
    node = stack.pop()

    visited[node - 1] = True
    for neighbor in graph[node]:
        if not visited[neighbor - 1]:
            stack.append(neighbor)
            family[neighbor - 1] = family[node - 1] + 1

print(family[target_2 - 1] - family[target_1 - 1])
