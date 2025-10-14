import sys

expression = list(sys.stdin.readline().rstrip())

answer = ''

stack = []
for exp in expression:
    if exp.isalpha():
        answer += exp
    else:
        if exp == '(':
            stack.append(exp)
        elif exp == '*' or exp == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(exp)
        elif exp == '+' or exp ==  '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(exp)
        elif exp == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
while stack:
    answer += stack.pop()
print(answer)