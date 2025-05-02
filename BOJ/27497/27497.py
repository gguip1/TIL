import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

string = deque()
last_append_index = []

for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    
    if len(command) == 1:
        if len(string) > 0:
            index = last_append_index.pop()
            if index == -1:
                string.pop()
            else:
                string.popleft()
    else:
        c, a = command
        c = int(c)
        if c == 1:
            string.append(a)
            last_append_index.append(-1)
        elif c == 2:
            string.appendleft(a)
            last_append_index.append(0)

if len(string) > 0:
    for s in string:
        print(s, end='')
    print()
else:
    print(0)