import sys

N = int(sys.stdin.readline().strip())

result = ''

while N > 1:
    result = str(N % 2) + result
    N //= 2

print(str(N) + result)
