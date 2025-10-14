import sys
input = sys.stdin.readline

N, T = map(int, input().split())

answer = float('inf')

for _ in range(N):
    S, I, C = map(int, input().split())

    for idx in range(C):
        if S + I * idx >= T:
            answer = min(answer, (S + idx * I) - T)

if answer == float('inf'):
    print(-1)
else:
    print(answer)
