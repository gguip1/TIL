import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    Q = sys.stdin.readline().rstrip()
    
    num = -1
    notCount = 0
    
    for q in Q:
        if q == '0' or q == '1':
            num = int(q)
            continue
        
        if num == -1:
            notCount += 1
        else:
            num = 1
            break
    
    if notCount % 2 == 0 and num == 0:
        print(0)
    elif notCount % 2 == 0 and num == 1:
        print(1)
    elif notCount % 2 != 0 and num == 0:
        print(1)
    elif notCount % 2 != 0 and num == 1:
        print(0)
        