import sys

hour, minute = map(int, sys.stdin.readline().strip().split())

minute += int(sys.stdin.readline().strip())

while minute > 59:
    minute -= 60
    hour += 1

while hour > 23:
    hour -= 24

print(hour, minute)
