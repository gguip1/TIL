import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

def check_ㅓ(y, x):
    check_lists = [[(1, 0), (1, -1), (1, 1)], [(-1, 1), (0, 1), (1, 1)], [(-1, -1), (0, -1), (1, -1)], [(-1, 0), (-1, -1), (-1, 1)]]
    results = []
    
    for check_list in check_lists:
        result = paper[y][x]
        is_result = True
        for c_y, c_x in check_list:
            if 0 <= (c_y + y) < N and 0 <= (c_x + x) < M:
                result += paper[c_y + y][c_x + x]
            else:
                is_result = False
                break
        if is_result:
            results.append(result)
    
    if results:
        return max(results)
    else:
        return 0

def dfs(y, x, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return
    deltas = [(1, 0),(-1, 0),(0, 1),(0, -1)]
    for dy, dx in deltas:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny, nx, depth + 1, total + paper[ny][nx])
            visited[ny][nx] = False

visited = [[False] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        answer = max(answer, check_ᅥ(y, x))
        visited[y][x] = True
        dfs(y, x, 1, paper[y][x])
        visited[y][x] = False

print(answer)