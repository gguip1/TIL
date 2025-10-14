import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

prefixSum = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        prefixSum[i] = nums[i] % M
    else:
        prefixSum[i] = (prefixSum[i - 1] + nums[i]) % M

remainderCheck = [0 for _ in range(M)]

for p in prefixSum:
    remainderCheck[p] += 1

count = 0

for index in range(M):
    if index == 0:
        count += remainderCheck[index]
    count += (remainderCheck[index] * (remainderCheck[index] - 1)) // 2

print(count)

# # 시간 초과 예상 O(N^2)
# count = 0

# for r in range(N):
#     if r == 0:
#         for i in range(N):
#             if nums[i] % M == 0:
#                 count += 1
#     else:
#         for i in range(N - r):
#             if i == 0:
#                 if prefixSum[r] % M == 0:
#                     count += 1
#             else:
#                 if (prefixSum[r + i] - prefixSum[i - 1]) % M == 0:
#                     count += 1

# print(count)