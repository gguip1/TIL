import sys

N = int(sys.stdin.readline().strip())

strs = []

for i in range(N):
    strs.append(sys.stdin.readline().strip())

strs = set(strs)
strs = list(strs)

strs.sort()
strs.sort(key = len )

for s in strs:
    print(s)
