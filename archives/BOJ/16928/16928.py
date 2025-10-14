import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ladders_snakes = [tuple(map(int, input().split())) for _ in range(N + M)]

queue = [(0, 0)]
visited = [False] * 100
visited[0] = True

answer = float('inf')

while queue:
    node_position, node_value = queue.pop(0)
    
    if node_position == 99:
        answer = node_value
        break
    
    deltas = [1, 2, 3, 4, 5, 6]
    
    for delta in deltas:
        if 0 <= node_position + delta < 100 and not visited[node_position + delta]:
            is_ladder_or_snake = False
            
            for ls in ladders_snakes:
                if (ls[0] - 1) == node_position + delta:
                    queue.append(((ls[1] - 1), node_value + 1))
                    visited[(ls[1] - 1)] = True
                    is_ladder_or_snake = True
                    break
            
            if not is_ladder_or_snake:
                queue.append((node_position + delta, node_value + 1))
                visited[node_position + delta] = True

print(answer)