import sys

S = sys.stdin.readline().strip()

KOREA = list('KOREA')

index = 0

for s in S:
    if KOREA[index % 5] == s:
        index += 1

print(index)
