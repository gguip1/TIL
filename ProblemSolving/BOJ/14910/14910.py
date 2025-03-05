import sys

nums = map(int, sys.stdin.readline().split())

def is_ascend(nums):
    prev_num = None
    for num in nums:
        if prev_num is None:
            prev_num = num
            continue
        
        if prev_num > num:
            return False
        
        prev_num = num
        
    return True

if is_ascend(nums):
    print('Good')
else:
    print('Bad')
