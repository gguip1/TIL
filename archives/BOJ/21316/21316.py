import sys
input = sys.stdin.readline

graph = {}

for _ in range(12):
    a, b = map(int, input().split())
    if graph.get(a) is None:
        graph[a] = [b]
    else:
        graph[a].append(b)
    
    if graph.get(b) is None:
        graph[b] = [a]
    else:
        graph[b].append(a)

for k, v in graph.items():
    c_1 = 0
    c_2 = 0
    c_3 = 0
    
    for _ in v:
        if len(graph[_]) == 1:
            c_1 += 1
        if len(graph[_]) == 2:
            c_2 += 1
        if len(graph[_]) == 3:
            c_3 += 1
    
    if c_1 == 1 and c_2 == 1 and c_3 == 1:
        print(k)
        sys.exit()
