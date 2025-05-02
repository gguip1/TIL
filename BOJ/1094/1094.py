X = int(input())

base = 64

while True:
    
    if base > X:
        base = base >> 1
    else:
        break
    

count = 1

start = base

while True:
    
    if start == X:
        break
    
    base = base >> 1
    
    if start + base <= X:
        start += base
        count += 1
    else:
        continue

print(count)