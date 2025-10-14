import sys

N, T, G = map(int, sys.stdin.readline().rstrip().split())

MAX = 100000
queue = []
queue.append((N, 0))
visited = [False] * MAX
visited[N] = True

while queue:
    node_n, node_t = queue.pop(0)
    
    if node_n == G:
        print(node_t)
        sys.exit(0)
    
    if node_t < T and node_n + 1 < MAX:
        if not visited[node_n + 1]:
            visited[node_n + 1] = True
            queue.append((node_n + 1, node_t + 1))

    digits = len(str(node_n * 2))
    if node_n > 0:
        if node_t < T and node_n * 2 < MAX and node_n * 2 - (10 ** (digits - 1)) < MAX:
            if not visited[node_n * 2 - (10 ** (digits - 1))] and node_n > 0:
                visited[node_n * 2 - (10 ** (digits - 1))] = True
                queue.append((node_n * 2 - (10 ** (digits - 1)), node_t + 1))

print('ANG')