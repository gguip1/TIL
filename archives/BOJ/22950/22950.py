import sys

N = int(sys.stdin.readline())
M = sys.stdin.readline().rstrip()
K = int(sys.stdin.readline())

if K == 0 or '1' not in list(M)[-K:]:
    print('YES')
else:
    print('NO')