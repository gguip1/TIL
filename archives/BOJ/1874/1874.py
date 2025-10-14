import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
index = 1

for _ in range(n):
    num = int(input())
    
    while not stack or stack[-1] != num:
        stack.append(index)
        answer.append('+')
        index += 1
        if index > n:
            break
    
    while stack and stack[-1] == num:
        stack.pop()
        answer.append('-')

if stack:
    print('NO')
else:
    print(*answer, sep='\n')