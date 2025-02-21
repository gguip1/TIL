import sys

M = sys.stdin.readline().strip().split("|")

A_Major = 0
C_Major = 0

A = ['A', 'D', 'E']
C = ['C', 'F', 'G']

for m in M:
    if m[0] in A:
        A_Major += 1
    elif m[0] in C:
        C_Major += 1

if A_Major > C_Major:
    print('A-minor')
elif C_Major > A_Major:
    print('C-major')
else:
    last_m = M[len(M) - 1][len(M[len(M) - 1]) - 1]
    if last_m in A:
        print('A-minor')
    elif last_m in C:
        print('C-major')
