import sys

M = int(sys.stdin.readline())

def check(_list, _num):
    result = False
    for _ in _list:
        if _ == _num:
            result = True
            break
    return result

result = []

for i in range(M):
    Q = sys.stdin.readline().strip()
    
    if Q == 'all' or Q == 'empty':
        calc = Q
    else:
        calc, val = Q.split()
        val = int(val)
    
    if calc == 'add':
        if check(result, val):
            continue
        else:
            result.append(val)
    elif calc == 'remove':
        if check(result, val):
            result.remove(val)
        else:
            continue
    elif calc == 'check':
        if check(result, val):
            print(1)
        else:
            print(0)
    elif calc == 'toggle':
        if check(result, val):
            result.remove(val)
        else:
            result.append(val)
    elif calc == 'all':
        result = [(x + 1) for x in range(20)]
    elif calc == 'empty':
        result = []
