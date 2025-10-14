import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s_num = str(bin(int(input())))

    x, y = 0, 0
    length = len(s_num[2:])
    
    for idx, s in enumerate(s_num[2:]):        
        if y == 0 and s == '1':
            y = length - idx - 1
            continue
        
        if x == 0 and s == '1':
            x = length - idx - 1
            continue
    
    print(x, y)