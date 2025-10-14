import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print('yes')
    
## 6 5
# 6 = 6 * (-1) * (-1) * (1)
# 5 = 6 - 1 - 1 + 1