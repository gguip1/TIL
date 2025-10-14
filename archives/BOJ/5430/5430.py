import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    x = input().strip()[1:-1]
    x = deque(map(int, x.split(','))) if x else deque()
    
    reverse = False
    
    try:
        for command in p:
            if command == 'R':
                reverse = not reverse
            else:
                if not reverse:
                    x.popleft()
                else:
                    x.pop()
                    
        if reverse:
            x.reverse()
        
        print('[', end='')
        print(*x, sep=',', end='')
        print(']')
    except:
        print('error')
