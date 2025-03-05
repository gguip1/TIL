import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

# for _ in range(M):
#     i, j = map(int, sys.stdin.readline().strip().split())
#     print(sum(nums[i - 1 : j]))

# sums = [[sum(nums[i : j + 1]) for j in range(N)] for i in range(N)]

# for _ in range(M):
#     i, j = map(int, sys.stdin.readline().strip().split())
#     print(sums[i - 1][j - 1])

sums = [0] * N

for i in range(N):
    if i == 0:
        sums[i] = nums[i]
        continue
    sums[i] = sums[i - 1] + nums[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    if i == 1:
        print(sums[j - 1])
    else:
        print(sums[j - 1] - sums[i - 2])