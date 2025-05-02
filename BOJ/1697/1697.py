import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

MAX = 100001
queue = [N]
seconds = [0] * MAX
visited = [False] * MAX
visited[N] = True

while queue and not visited[K]:
    node = queue.pop(0)
    
    if 0 <= node - 1 and not visited[node - 1]:
        seconds[node - 1] = seconds[node] + 1
        visited[node - 1] = True
        queue.append(node - 1)
    
    if node + 1 < MAX and not visited[node + 1]:
        seconds[node + 1] = seconds[node] + 1
        visited[node + 1] = True
        queue.append(node + 1)
    
    if node * 2 < MAX and not visited[node * 2]:
        seconds[node * 2] = seconds[node] + 1
        visited[node * 2] = True
        queue.append(node * 2)

print(seconds[K])