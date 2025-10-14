import sys

S = set()

M = int(sys.stdin.readline().strip())

for i in range(M):
    Q = sys.stdin.readline().strip()
    
    if Q == 'all':
        S = set([(x + 1) for x in range(20)])
    elif Q == 'empty':
        S = set()
    else:
        calc, val = Q.split()
        val = int(val)
        
        if calc == 'add':
            S.add(val)
        elif calc == 'remove':
            S.discard(val)
        elif calc == 'check':
            if val in S:
                print(1)
            else:
                print(0)
        elif calc == 'toggle':
            if val in S:
                S.discard(val)
            else:
                S.add(val)
