import sys
input = sys.stdin.readline
N = int(input())

for idx in range(1, N):
    print(' ' * abs(N - idx), end='')
    print('*' * (idx * 2 - 1), end='')
    print()

print('*' * ((N - 1) * 2 + 1))

for idx in range(1, N):
    print(' ' * idx, end='')
    print('*' * ((N - idx) * 2 - 1), end='')
    print()
