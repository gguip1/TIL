import sys

L = int(sys.stdin.readline())

if L % 5 == 0:
    print(L // 5)
else:
    print(L // 5 + 1)
