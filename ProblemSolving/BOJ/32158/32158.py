import sys

N = int(sys.stdin.readline().strip())
S = list(sys.stdin.readline().strip())

C = []
P = []

for index, s in enumerate(S):
    if s == 'C':
        C.append(index)
    elif s == 'P':
        P.append(index)

while len(C) > 0 and len(P) > 0:
    temp = S[C[0]]
    S[C[0]] = S[P[0]]
    S[P[0]] = temp
    C.pop(0)
    P.pop(0)

for s in S:
    print(s, end='')
