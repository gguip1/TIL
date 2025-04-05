import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []

for i in range(N):
    while len(stack) != 0 and A[stack[-1]] < A[i] :
        A[stack.pop()] = A[i]
    
    stack.append(i)

while (len(stack) != 0):
    A[stack.pop()] = -1

print(*A)

# # 안봐도 시간 초과
# def NGE(index):
#     for i in range(index, N):
#         if A[i] > A[index]:
#             return A[i]
#     return -1

# for i in range(N):
#     print(NGE(i), end=' ')
