import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
sequence = list(map(int, input().split()))

prefix = sequence.copy()

for _ in range(1, N):
    prefix[_] = prefix[_ - 1] ^ prefix[_]

answer = 0

for _ in range(Q):
    s, e = map(int, input().split())
    if s == 1:
        val = prefix[e - 1]
    else:
        val = prefix[e - 1] ^ prefix[s - 2]

    answer ^= val

print(answer)