import sys

matchstick = int(sys.stdin.readline().rstrip())

count = 0

for a in range(1, matchstick // 3 + 1):
    for b in range(a, (matchstick - a) // 2 + 1):
        c = matchstick - a - b
        if b <= c and c < a + b:
            count += 1

print(count)