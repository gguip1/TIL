import sys

N = int(sys.stdin.readline().rstrip())
tree = {}
result = [0] * (N + 1)

for _ in range(N):
    tree[_ + 1] = []

for _ in range(N - 1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)
    
    while stack:
        node = stack.pop()

        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                result[neighbor] = node
                stack.append(neighbor)

dfs(1)

for r in result[2:]:
    print(r)