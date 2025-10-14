T = int(input())

result = []

for i in range(T):
    A, B = map(int, input().split())
    
    result.append(A + B)

for index, value in enumerate(result):
    print(value)
