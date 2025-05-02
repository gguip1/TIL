N = int(input())
nums = list(map(int, input().split()))

def is_prime(num):
    
    if num <= 1:
        return False
    
    for i in range(num):
        
        if i == 0 or i == 1:
            continue
        
        if num % i == 0:
            return False
    
    return True

result = []

for index, value in enumerate(nums):
    if is_prime(value):
        result.append(value)

print(len(result))