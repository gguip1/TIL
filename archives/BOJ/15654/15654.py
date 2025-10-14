import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()

def dfs(path):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(N):
        if nums[i] not in path:
            dfs(path + [nums[i]])

dfs([])