N = int(input())

def is_decom_sum(num, target):
    
    sum_ = num
    
    for i in range(len(str(num))):
        sum_ += int(str(num)[i])
    
    if sum_ == target:
        return True
    
    return False

result = 0

for i in range(N):
    if is_decom_sum(i, N):
        result = i
        break

print(result)
