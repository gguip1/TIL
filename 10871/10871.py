N, X = map(int, input().split())

A = list(map(int, input().split()))

for index, value in enumerate(A):
    
    if value < X:
        print(value, end=" ")
