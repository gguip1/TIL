import sys

Q = int(sys.stdin.readline().strip())

for _ in range(Q):
    a, m = map(int, sys.stdin.readline().strip().split())
    
    result = (a * m * 1056) // 600000
    print(result)