import sys
input = sys.stdin.readline

N = int(input())

orig = input().rstrip()
check = input().rstrip()

if N % 2 == 0:
    if orig == check:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    for idx in range(len(orig)):
        if orig[idx] == check[idx]:
            print('Deletion failed')
            sys.exit()

    print('Deletion succeeded')
