import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
sequence = list(map(int, input().split()))

shift = 0

for _ in range(Q):
    command = list(map(int, input().split()))

    match command[0]:
        case 1:
            i, x = command[1], command[2]
            idx = (shift + i - 1) % N
            sequence[idx] += x
        case 2:
            s = command[1] % N
            shift = (shift - s) % N
        case 3:
            s = command[1] % N
            shift = (shift + s) % N

for i in range(N):
    print(sequence[(shift + i) % N], end=' ')