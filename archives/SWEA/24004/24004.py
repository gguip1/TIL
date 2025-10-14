T = int(input())

def bfs(G, N):
    queue = []
    visited = [False] * N
    queue.append(0)
    visited[0] = True
    while queue:
        node = queue.pop(0)
        print(node)
        for i in range(N):
            pass

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))