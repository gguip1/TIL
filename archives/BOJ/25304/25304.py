import sys
input = sys.stdin.readline

X = int(input())
N = int(input())

cnt = 0
amt = 0

for _ in range(N):
    a, b = map(int, input().split())
    cnt += 1
    amt += a * b

if cnt == N and X == amt:
    print('Yes')
else:
    print('No')
