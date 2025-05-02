nums = map(int, input().split())

sum_ = 0

for index, value in enumerate(nums):
    
    sum_ += value ** 2

print(sum_ % 10)
