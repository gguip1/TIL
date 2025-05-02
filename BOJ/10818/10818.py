def min_in_nums(nums):
    
    min_ = None
    
    for index, value in enumerate(nums):
        if min_ is None:
            min_ = value
        
        if min_ > value:
            min_ = value
    
    return min_

def max_in_nums(nums):
    
    max_ = None
    
    for index, value in enumerate(nums):
        if max_ is None:
            max_ = value
        
        if max_ < value:
            max_ = value
    
    return max_


N = int(input())

nums = list(map(int, input().split()))

print(min_in_nums(nums), max_in_nums(nums))
