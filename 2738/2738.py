N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    B.append(list(map(int, input().split())))

A_B = []

for i in range(N):
    _B = []
    for j in range(M):
        _B.append(A[i][j] + B[i][j])
    A_B.append(_B)

for a_b in A_B:
    for _b in a_b:
        print(_b, end=' ')
    print()
