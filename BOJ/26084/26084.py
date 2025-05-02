import sys

S = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
handles = [sys.stdin.readline().rstrip()[0] for _ in range(N)]

S1 = 0
S2 = 0
S3 = 0

for handle in handles:
    if S[0] == handle:
        S1 += 1
    if S[1] == handle:
        S2 += 1
    if S[2] == handle:
        S3 += 1

import math

if S[0] != S[1] != S[2] != S[0]:
    print(S1 * S2 * S3)
elif S[0] == S[1] != S[2] != S[0]:
    if S1 - 2 >= 0:
        print(math.factorial(S1) // (math.factorial(S1 - 2) * math.factorial(2)) * S3)
    else:
        print(0)
elif S[0] != S[1] == S[2] != S[0]:
    if S1 - 2 >= 0:
        print(math.factorial(S2) // (math.factorial(S2 - 2) * math.factorial(2)) * S1)
    else:
        print(0)
elif S[0] == S[2] != S[1] != S[0]:
    if S1 - 2 >= 0:
        print(math.factorial(S1) // (math.factorial(S1 - 2) * math.factorial(2)) * S2)
    else:
        print(0)
elif S[0] == S[1] == S[2] == S[0]:
    if S1 - 3 >= 0:
        print(math.factorial(S1) // (math.factorial(S1 - 3) * math.factorial(3)))
    else:
        print(0)
