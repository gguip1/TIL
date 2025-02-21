import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    C = int(sys.stdin.readline().strip())
    
    Q, D, N, P = 0, 0, 0, 0
    
    while True:
        if C - 25 >= 0:
            Q += 1
            C = C - 25
        else:
            break
    
    while True:
        if C - 10 >= 0:
            D += 1
            C = C - 10
        else:
            break
    
    while True:
        if C - 5 >= 0:
            N += 1
            C = C - 5
        else:
            break
    
    while True:
        if C - 1 >= 0:
            P += 1
            C = C - 1
        else:
            break
    
    print(Q, D, N, P)
