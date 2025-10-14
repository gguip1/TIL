import sys
input = sys.stdin.readlines

def solve(n):
    r_v = 1
    if n == 0:
        return r_v
    else:
        for v in range(1, n + 1):
            r_v *= v
            while r_v != 0 and r_v % 10 == 0:
                r_v //= 10
    return r_v % 10

Ns = input()

for N in Ns:
    print(f'{int(N):>5} -> {solve(int(N))}')