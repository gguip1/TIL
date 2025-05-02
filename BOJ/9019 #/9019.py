import sys

def D(node):
    for i in range(4):
        node[i] = int(node[i]) * 2
    return node

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(list, sys.stdin.readline().rstrip().split())
    
    while len(A) < 4:
        A.insert(0, '0')
    
    while len(B) < 4:
        B.insert(0, '0')
    
    queue = [A]
    record = {}
    
    while queue:
        node = queue.pop(0)
        
        print(D(node))


