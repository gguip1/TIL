N = int(input())

list_ = [input() for x in range(N)]

result = None

for index, value in enumerate(list_):
    
    if result is None:
        result = list(value)
        continue
    
    for i in range(len(result)):
        
        if result[i] != value[i]:
            result[i] = '?'

print(''.join(result))
