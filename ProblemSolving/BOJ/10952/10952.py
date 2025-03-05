result = []

while True:
    A, B = map(int, input().split())
    
    if A == 0 and B == 0:
        break
    
    result.append(A + B)

for index, value in enumerate(result):
    print(value)
