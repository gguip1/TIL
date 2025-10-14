import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = [(num + 1) for num in range(N)]
targets = list(map(int, input().split()))

answer = 0

def check_target_index(target):
    for index, num in enumerate(nums):
        if target == num:
            return index
    

for target in targets:
    while nums[0] != target:
        target_index = check_target_index(target)
        if target_index <= abs(len(nums) - 1 - target_index):
            nums.append(nums.pop(0))
        else:
            nums = [nums[-1]] + nums[:-1]
        answer += 1
    
    if nums[0] == target:
        nums.pop(0)

print(answer)
