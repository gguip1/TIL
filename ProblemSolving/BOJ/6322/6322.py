import sys

def _6322(a, b, c, index):
    print(f'Triangle #{index}')
    
    if a == -1:
        if b < c:
            print(f'a = {((c ** 2 - b ** 2) ** 0.5):.3f}')
        else:
            print("Impossible.")
    elif b == -1:
        if a < c:
            print(f'b = {((c ** 2 - a ** 2) ** 0.5):.3f}')
        else:
            print("Impossible.")
    elif c == -1:
        print(f'c = {((a ** 2 + b ** 2) ** 0.5):.3f}')
    
    print()

index = 1

while True:
    a, b ,c = map(int, sys.stdin.readline().strip().split())

    if a == 0 and b == 0 and c == 0:
        break
    
    _6322(a, b, c, index)

    index += 1
