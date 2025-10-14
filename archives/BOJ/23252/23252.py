import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    
    if (C > 0 and A >= C and (C - A) % 2 == 0) or (C == 0 and A > 0 and A % 2 == 0) or (C == 0 and A == 0 and B % 2 == 0):
        print('Yes')
    else:
        print('No')
