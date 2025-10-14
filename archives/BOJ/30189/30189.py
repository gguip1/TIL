import sys

n, m = map(int, sys.stdin.readline().strip().split())

result = 0

for i in range(n + m + 1):
    for j in range(n + 1):
        for z in range(m + 1):
            if (j + z) == (i):
                result += 1

print(result)
