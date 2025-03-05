import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    op1, operator, op2, equal_op, result = sys.stdin.readline().strip().split()
    if operator == '+':
        if int(op1) + int(op2) == int(result):
            print('correct')
        else:
            print('wrong answer')
    elif operator == '-':
        if int(op1) - int(op2) == int(result):
            print('correct')
        else:
            print('wrong answer')
    elif operator == '*':
        if int(op1) * int(op2) == int(result):
            print('correct')
        else:
            print('wrong answer')
    elif operator == '/':
        if int(op1) / int(op2) == int(result):
            print('correct')
        else:
            print('wrong answer')