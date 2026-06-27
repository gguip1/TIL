def solution(nums):
    answer = 0
    p = {}
    
    for num in nums:
        p[num] = p.get(num, 0) + 1
    
    if len(p.keys()) >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(p.keys())
    
    return answer