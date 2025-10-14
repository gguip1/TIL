K = int(input())

result = []

for i in range(K):
    
    value = int(input())
    
    if value == 0:
        result.pop()
    else:
        result.append(value)

print(sum(result))
