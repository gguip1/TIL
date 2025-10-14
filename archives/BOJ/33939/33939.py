import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = 0
graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    if graph.get(v) is None:
        graph[v] = [u]
    else:
        graph[v].append(u)

for k, v in graph.items():
    if len(v) >= 2:
        for idx_1 in range(len(v) - 1):
            for idx_2 in range(idx_1 + 1, len(v)):
                if v[idx_2] not in graph.get(v[idx_1], []) and v[idx_1] not in graph.get(v[idx_2], []):
                    answer += 1

print(answer)
