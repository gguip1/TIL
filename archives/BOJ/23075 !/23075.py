import sys
matchsticks = int(sys.stdin.readline().rstrip())

if matchsticks % 2 == 0:
    print((matchsticks ** 2 + 22) // 48)
else:
    print(((matchsticks + 3) ** 2 + 24) // 48)