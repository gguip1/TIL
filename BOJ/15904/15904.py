import sys
input = sys.stdin.readline

string = input()
step = 0

for s in string:
    if step == 0 and s == 'U':
        step += 1
    elif step == 1 and s == 'C':
        step += 1
    elif step == 2 and s == 'P':
        step += 1
    elif step == 3 and s == 'C':
        step += 1

if step == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
