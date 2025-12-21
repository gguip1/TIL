import sys
input = sys.stdin.readline

N, B, C = map(int, input().split())
A = list(map(int, input().split())) + [0, 0]

def buy_3(idx):
    min_v = min(A[idx], A[idx + 1], A[idx + 2])
    A[idx] -= min_v
    A[idx + 1] -= min_v
    A[idx + 2] -= min_v
    return min_v * (B + 2 * C)

def buy_2(idx):
    min_v = min(A[idx], A[idx + 1])
    A[idx] -= min_v
    A[idx + 1] -= min_v
    return min_v * (B + C)

def buy_1(idx):
    min_v = A[idx]
    A[idx] -= min_v
    return min_v * B

answer = 0

for idx in range(N):
    if B < C:
        answer += buy_1(idx)
    else:
        if A[idx + 1] > A[idx + 2]:
            min_v = min(A[idx], A[idx + 1] - A[idx + 2])
            A[idx] -= min_v
            A[idx + 1] -= min_v
            answer += min_v * (B + C)
            answer += buy_3(idx)
            answer += buy_1(idx)
        else:
            answer += buy_3(idx)
            answer += buy_2(idx)
            answer += buy_1(idx)

print(answer)