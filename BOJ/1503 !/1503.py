import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
S = set(map(int, sys.stdin.readline().rstrip().split()))

num = 1001
min_value = float('inf')

for x in range(1, num):
    if x in S:
        continue
    for y in range(1, num):
        if y in S:
            continue
        for z in range(1, num):
            if z in S:
                continue
            min_value = min(min_value, abs(N - x * y * z))
            if N + 1 < x * y * z:
                break

print(min_value)
