result = []

while True:    
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        result.append('right')
    else:
        result.append('wrong')
    
for index, value in enumerate(result):
    print(value)
