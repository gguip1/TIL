import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split())) + [0, 0]

def buy_3(idx):
    min_v = min(A[idx], A[idx + 1], A[idx + 2])
    A[idx] -= min_v
    A[idx + 1] -= min_v
    A[idx + 2] -= min_v
    return min_v * 7

def buy_2(idx):
    min_v = min(A[idx], A[idx + 1])
    A[idx] -= min_v
    A[idx + 1] -= min_v
    return min_v * 5

def buy_1(idx):
    min_v = A[idx]
    A[idx] -= min_v
    return min_v * 3

answer = 0

for idx in range(N):
    if A[idx + 1] > A[idx + 2]:
        min_v = min(A[idx], A[idx + 1] - A[idx + 2])
        A[idx] -= min_v
        A[idx + 1] -= min_v
        answer += min_v * 5
        answer += buy_3(idx)
        answer += buy_1(idx)
    else:
        answer += buy_3(idx)
        answer += buy_2(idx)
        answer += buy_1(idx)

print(answer)