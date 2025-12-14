from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if graph.get(u) is None:
        graph[u] = [v]
    else:
        graph[u].append(v)

S = int(input())
S_nums = list(map(int, input().split()))
fans = [False] * N

for num in S_nums:
    fans[num - 1] = True

answer = False

if not fans[0]:
    queue = deque([0])

    while queue:
        node = queue.popleft()

        paths = graph.get(node + 1)

        if paths:
            for path in paths:
                if not fans[path - 1]:
                    queue.append(path - 1)
        else:
            if not fans[node]:
                answer = True

if answer:
    print('yes')
else:
    print('Yes')
