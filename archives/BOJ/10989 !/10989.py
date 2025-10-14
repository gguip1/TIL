import sys

N = int(sys.stdin.readline())

nums = [0 for _ in range(10000)]

for i in range(N):
    nums[int(sys.stdin.readline()) - 1] += 1

for i, n in enumerate(nums):
    for _ in range(n):
        print(i + 1)
