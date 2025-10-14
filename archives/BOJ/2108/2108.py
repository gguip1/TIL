import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()
nums_count = {}
for num in nums:
    if nums_count.get(num) is None:
        nums_count[num] = 1
    else:
        nums_count[num] += 1

mode_num_count = 0
mode_num_list = []
for key, value in nums_count.items():
    if value > mode_num_count:
        mode_num_count = value
        mode_num_list = [key]
    elif value == mode_num_count:
        mode_num_list.append(key)

print(round(sum(nums) / len(nums)))
print(nums[len(nums) // 2])
print(mode_num_list[0] if len(mode_num_list) == 1 else mode_num_list[1])
print(max(nums) - min(nums))
