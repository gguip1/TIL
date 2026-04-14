import sys
input = sys.stdin.readline

N, M = map(int, input().split())

regions = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

stack = []

for y in range(N):
    for x in range(M):
        match regions[y][x]:
            case '@':
                stack.append((y, x))
            case '*':
                visited[y][x] = 1
            case '#':
                visited[y][x] = 2

sy, sx = stack.pop()

for d in range(1, 3):
    if sy + d >= N or regions[sy + d][sx] == "|":
        break
    if (regions[sy + d][sx] == '*' and visited[sy + d][sx] > 0) or (regions[sy + d][sx] == '#' and visited[sy + d][sx] > 0):
        visited[sy + d][sx] -= 1
        if visited[sy + d][sx] == 0:
            stack.append((sy + d, sx))

for d in range(1, 3):
    if sy - d < 0 or regions[sy - d][sx] == "|":
        break
    if (regions[sy - d][sx] == '*' and visited[sy - d][sx] > 0) or (regions[sy - d][sx] == '#' and visited[sy - d][sx] > 0):
        visited[sy - d][sx] -= 1
        if visited[sy - d][sx] == 0:
            stack.append((sy - d, sx))

for d in range(1, 3):
    if sx + d >= M or regions[sy][sx + d] == "|":
        break
    if (regions[sy][sx + d] == '*' and visited[sy][sx + d] > 0) or (regions[sy][sx + d] == '#' and visited[sy][sx + d] > 0):
        visited[sy][sx + d] -= 1
        if visited[sy][sx + d] == 0:
            stack.append((sy, sx + d))

for d in range(1, 3):
    if sx - d < 0 or regions[sy][sx - d] == "|":
        break
    if (regions[sy][sx - d] == '*' and visited[sy][sx - d] > 0) or (regions[sy][sx - d] == '#' and visited[sy][sx - d] > 0):
        visited[sy][sx - d] -= 1
        if visited[sy][sx - d] == 0:
            stack.append((sy, sx - d))

while stack:
    ny, nx = stack.pop()

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= ny + dy < N and 0 <= nx + dx < M and regions[ny + dy][nx + dx] != '|':
            if (regions[ny + dy][nx + dx] == '*' and visited[ny + dy][nx + dx] > 0) or (regions[ny + dy][nx + dx] == '#' and visited[ny + dy][nx + dx] > 0):
                visited[ny + dy][nx + dx] -= 1
                if visited[ny + dy][nx + dx] == 0:
                    stack.append((ny + dy, nx + dx))

answer = [0, 0]

for y in range(N):
    for x in range(M):
        if (regions[y][x] == '*' or regions[y][x] == '#') and visited[y][x] == 0:
            answer[0] += 1
        if (regions[y][x] == '*' or regions[y][x] == '#') and visited[y][x] != 0:
            answer[1] += 1

print(*answer)
