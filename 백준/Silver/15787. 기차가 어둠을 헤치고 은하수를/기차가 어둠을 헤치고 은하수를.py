import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trains = [0 for _ in range(N)]

mask = (1 << 20) - 1

for _ in range(M):
    command = list(map(int, input().split()))

    i = command[1]

    match command[0]:
        case 1:
            x = command[2]
            trains[i - 1] |= 1 << (x - 1)
        case 2:
            x = command[2]
            trains[i - 1] &= ~(1 << (x - 1))
        case 3:
            trains[i - 1] <<= 1
        case 4:
            trains[i - 1] >>= 1
    
    trains[i - 1] &= mask

print(len(set(trains)))