import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

if 100 * N >= M:
    print('Yes')
else:
    print('No')