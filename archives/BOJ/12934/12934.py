import sys
import math

x, y = map(int, sys.stdin.readline().rstrip().split())

def solve(x, y):
    s = x + y
    D = 1 + 8 * s
    sqrt_D = int(math.isqrt(D))

    if sqrt_D * sqrt_D != D:
        return -1

    n = (-1 + sqrt_D) // 2
    if n * (n + 1) // 2 == s:
        return n
    return -1

n = solve(x, y)
if n != -1:
    count = 0
    for j in range(n, 0, -1):
        if x >= j:
            x -= j
            count += 1
    print(count)
else:
    print(-1)