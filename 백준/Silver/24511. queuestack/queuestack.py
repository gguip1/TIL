import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

# for n in range(M):
#     t = C[n]
#     for idx in range(N):
#         if A[idx] == 0:
#             t, B[idx] = B[idx], t
#     print(t, end=' ')

for idx in range(N - 1, -1, -1):
    if M == 0:
        break
    if A[idx] == 0:
        print(B[idx], end=' ')
        M -= 1

if M != 0:
    for idx in range(M):
        print(C[idx], end=' ')