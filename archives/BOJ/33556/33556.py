import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

if A == 'null':
    print('NullPointerException')
    print('NullPointerException')
else:
    if B == 'null':
        print('false')
        print('false')
    else:
        if A == B:
            print('true')
        else:
            print('false')
        
        if A.lower() == B.lower():
            print('true')
        else:
            print('false')
