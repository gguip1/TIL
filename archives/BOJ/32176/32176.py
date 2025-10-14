import sys

def get_p(a, b, c, d):
    return abs(a - c) + abs(b - d)

def get_u(a, b, c, d):
    return (abs(a - c) + 1) * (abs(b - d) + 1)

def get_c(p, u):
    return max(p - u, 0)

N, M, K_1, K_2 = map(int, sys.stdin.readline().rstrip().split())
town = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


