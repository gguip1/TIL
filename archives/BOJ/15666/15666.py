import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

def solve(ns: list, idx: int):
    if M == len(ns):
        print(*ns)
        return
    
    for _idx, num in enumerate(nums):
        if _idx >= idx:
            solve(ns + [num], _idx)

for idx, num in enumerate(nums):
    solve([num], idx)
