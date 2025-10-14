import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
answer = [0] * N

for i in range(N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0] + 1 
    stack.append((i, towers[i]))
    
print(*answer)


## 시간 초과
# N = int(input())
# towers = list(map(int, input().split()))
# answer = [0] * N

# while towers:
#     current = towers.pop()

#     for idx in range(len(towers) - 1, -1, -1):
#         if towers[idx] >= current:
#             answer[len(towers)] = idx + 1
#             break

# print(*answer)
