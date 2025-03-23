import sys

N, K, M = map(int, sys.stdin.readline().rstrip().split())
Ls = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

Ls.sort()

left, right = 0, len(Ls) - 1
mid = len(Ls) // 2

while len(Ls[left:right]) > 1:
    if Ls[mid] >= K:
        mid += len(Ls[mid:right])
        left = mid
    elif Ls[mid] < K:
        mid -= len(Ls[left:mid])
        right = mid

print(Ls[left:right + 1])

# P = 0

# for L in Ls:
#     if L < 2 * K:
#         L -= K
#     elif L <= K:
#         continue
#     else:
#         L -= (2 * K)
    
#     if (L // M) > P:
#         P = L // M

# if P == 0:
#     print(-1)
# else:
#     print(P)