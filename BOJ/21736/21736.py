import sys
input = sys.stdin.readline

N, M = map(int, input().split())
campus = list(list(input().strip()) for _ in range(N))
visited = [[False] * M for _ in range(N)] 

def where_is_doyeon():
    for y in range(N):
        for x in range(M):
            if campus[y][x] == 'I':
                return (y, x)

answer = 0

doyeon_y, doyeon_x = where_is_doyeon()

stack = [(doyeon_y, doyeon_x)]
visited[doyeon_y][doyeon_x] = True

while stack:
    node_y, node_x = stack.pop()
    
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dy, dx in deltas:
        y, x = node_y + dy, node_x + dx
        if 0 <= y < N and 0 <= x < M and not visited[y][x]:
            if campus[y][x] != 'X':
                stack.append((y, x))
                visited[y][x] = True
            if campus[y][x] == 'P':
                answer += 1

if answer != 0:
    print(answer)
else:
    print('TT')
