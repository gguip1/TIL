import sys

# N = list(map(int, list(sys.stdin.readline().strip())))

N = int(sys.stdin.readline().strip())

digits = [0] * 10

for i in range(1, N + 1):
    for n in list(map(int, list(str(i)))):
        digits[n] += 1

print(*digits)
