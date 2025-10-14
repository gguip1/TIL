import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deque_ = deque()

for _ in range(N):
    commands = input().split()
    
    match commands[0]:
        case 'push_front':
            deque_.appendleft(commands[1])
        case 'push_back':
            deque_.append(commands[1])
        case 'pop_front':
            if deque_:
                print(deque_.popleft())
            else:
                print(-1)
        case 'pop_back':
            if deque_:
                print(deque_.pop())
            else:
                print(-1)
        case 'size':
            print(len(deque_))
        case 'empty':
            if deque_:
                print(0)
            else:
                print(1)
        case 'front':
            if deque_:
                print(deque_[0])
            else:
                print(-1)
        case 'back':
            if deque_:
                print(deque_[-1])
            else:
                print(-1)
