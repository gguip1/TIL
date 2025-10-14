import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = A.copy()
B.sort()

P = []

for a in A:
    for index, b in enumerate(B):
        if a == b and index not in P:
            P.append(index)
            break

print(*P)