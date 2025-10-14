import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = {}

for _ in range(M):
    a, b = map(int, input().split())
    
    tree[a] = [b] if tree.get(a) is None else tree.get(a) + [b]
    tree[b] = [a] if tree.get(b) is None else tree.get(b) + [a]

min_val = float('inf')
answer = 0

for num in range(1, N + 1):
    queue = [(num, 0)]
    relation = [0] * N
    
    score = 0
    while queue:
        node_num, node_score = queue.pop(0)
        
        for next in tree[node_num]:
            if next != num and relation[next - 1] == 0:
                queue.append((next, node_score + 1))
                relation[next - 1] = node_score + 1
    
    kevin_bacon = sum(relation)
    if min_val > kevin_bacon:
        min_val = kevin_bacon
        answer = num
    
print(answer)