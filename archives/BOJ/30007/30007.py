N = int(input())

W_list = []

for i in range(N):
    
    A, B, X = map(int, input().split())
    
    W = A * (X - 1) + B
    
    W_list.append(W)

for index, value in enumerate(W_list):
    print(value)
