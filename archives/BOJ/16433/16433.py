import sys
input = sys.stdin.readline

N, R, C = map(int, input().split())

check = (R + C) % 2 == 0

for i in range(N):
    for j in range(N):
        if check:
            if i % 2 == 0:
                print('v' if j % 2 == 0 else '.', end='')
            else:
                print('.' if j % 2 == 0 else 'v', end='')
        else:
            if i % 2 == 0:
                print('.' if j % 2 == 0 else 'v', end='')
            else:
                print('v' if j % 2 == 0 else '.', end='')
    print()