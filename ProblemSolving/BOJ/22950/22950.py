import sys

N = int(sys.stdin.readline())
M = sys.stdin.readline().rstrip()
K = int(sys.stdin.readline())

if N <= K:
    if '1'in list(M):
        print('NO')
    else:
        print('YES')
else:
    if '1' in list(M)[-K:]:
        print('NO')
    else:
        print('YES')
