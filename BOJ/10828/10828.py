import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = input().strip().split()
    
    match command[0]:
        case 'push': stack.append(int(command[1]))
        case 'pop': print(stack.pop()) if stack else print(-1)
        case 'size': print(len(stack))
        case 'empty': print(0) if stack else print(1)
        case 'top':print(stack[-1]) if stack else print(-1)
    
