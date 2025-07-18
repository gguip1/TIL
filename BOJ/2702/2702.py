import sys

def least(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i
    
def greatest(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(least(a, b), greatest(a, b))
