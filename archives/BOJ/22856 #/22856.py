import sys

N = int(sys.stdin.readline().rstrip())

left_graph = {
    
}

right_graph = {
    
}

visited = [False] * N

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    
    left_graph[a] = b
    right_graph[a] = c

parents = []
now = 1
visited_count = 1
count = 0

while visited_count < N:
    if left_graph[now] != -1 and not visited[left_graph[now] - 1]:
        parents.append(now)
        now = left_graph[now]
    elif right_graph[now] != -1 and not visited[right_graph[now] - 1]:
        parents.append(now)
        now = right_graph[now]
    else:
        visited[now - 1] = True
        visited_count += 1
        now = parents.pop()
    count += 1

now = 1

while True:
    now = right_graph[now]
    if now != -1:
        count -= 1
    else:
        break

print(count)
