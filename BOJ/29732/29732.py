import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
S = list(input())

for i in range(N):
    if S[i] == 'R':
        for r in range(max(1, i + 1 - K), min(N, i + 1 + K) + 1):
            S[r] = 'R'

count = 0
for i in range(N):
    if S[i] == 'R':
        count += 1

if M - count >= 0:
    print('Yes')
else:
    print('No')
