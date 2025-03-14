import sys

def dac(A, B, C):
    if B == 0:
        return 1
    elif B == 1:
        return A % C
    
    K =  dac(A, B // 2, C) % C
    if B % 2 == 0:
        return K * K % C
    else:
        return K * K % C * A % C
        

A, B, C = map(int, sys.stdin.readline().rstrip().split())

print(dac(A, B, C))