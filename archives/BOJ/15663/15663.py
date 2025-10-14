from itertools import *
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = sorted(set(list(permutations(map(int, input().split()), M))))
for answer in nums:
    print(*answer)