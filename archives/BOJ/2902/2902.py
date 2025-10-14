import sys
input = sys.stdin.readline

name = input().split('-')

for n in name:
    print(n[0], end='')
