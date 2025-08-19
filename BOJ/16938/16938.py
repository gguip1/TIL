import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

visited = [False] * N
answer = 0

def solve(selected:list = []):
    global answer
    if len(selected) >= 2 and R >= sum(selected) >= L and max(selected) - min(selected) >= X:
        answer += 1
    check_idx = 0
    for idx in range(N):
        if visited[idx]:
            check_idx = idx
    for idx in range(check_idx, N):
        if not visited[idx]:
            visited[idx] = True
            solve(selected + [A[idx]])
            visited[idx] = False
solve()
print(answer)
