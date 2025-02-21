import sys

S = []

while True:
    s = sys.stdin.readline().replace('\n', '')
    if s == '.':
        break
    else:
        S.append(s)

for s in S:
    check = []
    for v in s:
        if v == '(':
            check.append('(')
        elif v == ')':
            if check:
                if check[len(check) - 1] == '(':
                    check.pop(len(check) - 1)
                else:
                    break
            else:
                check.append(')')
                break
        elif v == '[':
            check.append('[')
        elif v == ']':
            if check:
                if check[len(check) - 1] == '[':
                    check.pop(len(check) - 1)
                else:
                    break
            else:
                check.append(']')
                break
        
    if len(check) != 0:
        print('no')
    else:
        print('yes')
