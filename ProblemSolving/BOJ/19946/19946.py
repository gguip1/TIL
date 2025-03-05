N = int(input())

for i in range(65):
    check = 2 ** i - 1
    
    for j in range(i, 65):
        N_check = check * 2 ** (j - i)
    
    if N == N_check:
        print(i)
        break