import sys

N = int(sys.stdin.readline().strip())

check = list(map(int, sys.stdin.readline().strip().split()))

print(min(check) * max(check))
