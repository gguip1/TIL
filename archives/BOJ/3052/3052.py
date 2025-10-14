remainders = []

def is_diff(n):
    
    is_ = True
    
    for val in remainders:
        if val == n:
            is_ = False
            
    return is_

nums = []

for i in range(10):
    nums.append(int(input()))

for num in nums:
    remainder = num % 42
    if is_diff(remainder):
        remainders.append(remainder)

print(len(remainders))
