import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

print(26 * (N + 1) - N)
