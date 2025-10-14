import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    a_path = [A]
    b_path = [B]
    
    while A != 1:
        A //= 2
        a_path.append(A)
    
    while B != 1:
        B //= 2
        b_path.append(B)
    
    for idx in range(len(a_path)):
        if a_path[idx] in b_path:
            print(a_path[idx] * 10)
            break
            
