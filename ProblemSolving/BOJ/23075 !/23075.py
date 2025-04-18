import sys
matchsticks = int(sys.stdin.readline().rstrip())
print((matchsticks ** 2 + 6 * matchsticks * (matchsticks % 2) + 22) // 48)