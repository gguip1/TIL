import sys

N = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for x in range(N)]

for i in range(N - 1):
    for j in range(N - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
    print(num)
