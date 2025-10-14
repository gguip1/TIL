import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    command = input().strip().split()
    
    match command[0]:
        case 'push': queue.append(int(command[1]))
        case 'pop': print(queue.pop(0) if queue else -1)
        case 'size': print(len(queue))
        case 'empty': print(0 if queue else 1)
        case 'front': print(queue[0] if queue else -1)
        case 'back': print(queue[-1] if queue else -1)
