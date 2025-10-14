import sys

Q = int(sys.stdin.readline().strip())

MIN = -(10 ** 18)
MAX = 10 ** 18

up = MIN - 1
down = MAX + 1
paradox = False
find = False
result = 0

for index in range(Q):
    num, info = sys.stdin.readline().strip().split()
    num = int(num)
    
    if not paradox:
        if info == '^' and num > up:
            up = num
        elif info == '^' and num == MAX:
            paradox = True
            result = index + 1
            continue
        
        if info == 'v' and num < down:
            down = num
        elif info == 'v' and num == MIN:
            paradox = True
            result = index + 1
            continue
        
        if up >= down - 1:
            paradox = True
            result = index + 1
            continue
        
        if not find and up == down - 2:
            find = True
            result = index + 1
            continue

if paradox:
    print('Paradox!')
    print(result)
else:
    if find:
        print('I got it!')
        print(result)
    else:
        print('Hmm...')