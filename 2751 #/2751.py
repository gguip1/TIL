import sys
from Sort import BubbleSort

N = int(sys.stdin.readline().strip())

nums = []

for i in range(N):
    num = int(sys.stdin.readline().strip())
    nums.append(num)

print(nums)

for num in nums:
    print(num)

# Case:1 sort...? 이건 좀
# N = int(sys.stdin.readline().strip())

# nums = []

# for i in range(N):
#     num = int(sys.stdin.readline().strip())
#     nums.append(num)

# nums.sort()

# for num in nums:
#     print(num)
