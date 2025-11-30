import sys
input = sys.stdin.readline

f_string = input().rstrip()
s_string = list(input().rstrip())

stack = []

for idx in range(len(f_string)):
    stack.append(f_string[idx])

    while len(stack) >= len(s_string) and stack[-len(s_string):] == s_string:
        for _ in range(len(s_string)):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')