import sys
input = sys.stdin.readline

def dfs(path:list):
    if len(path) == M:
        print(*path)
        return
    
    for num in range(1, N + 1):
        if num in path:
            continue

        path.append(num)
        dfs(path)
        path.pop()

N, M = map(int, input().split())

dfs([])
