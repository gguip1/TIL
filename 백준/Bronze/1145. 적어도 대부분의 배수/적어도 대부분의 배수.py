import sys
input = sys.stdin.readline
a, b, c, d, e = map(int, input().split())

for n in range(1, a * b * c * d * e + 1):
    cnt = 0
    if n % a == 0:
        cnt += 1
    if n % b == 0:
        cnt += 1
    if n % c == 0:
        cnt += 1
    if n % d == 0:
        cnt += 1
    if n % e == 0:
        cnt += 1
    if cnt >= 3:
        print(n)
        break