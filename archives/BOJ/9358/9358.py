import sys

input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    
    seq = list(map(int, input().strip().split()))
    
    while True:
        if N == 2:
            break
        
        if N % 2 == 0:
            for j in range(N // 2):
                seq[j] += seq[(N - 1) - j]
            N //= 2
            seq = seq[:N]
        else:
            for j in range(N // 2):
                seq[j] += seq[(N - 1) - j]
            seq[j + 1] += seq[j + 1]
            N = (N // 2) + 1
            seq = seq[:N]
        
    if seq[0] > seq[1]:
        print(f'Case #{i + 1}: Alice')
    else:
        print(f'Case #{i + 1}: Bob')
            
