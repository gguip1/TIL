import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

def check():
    for a in A:
        if a > K:
            print(answer)
            sys.exit()

for a in A:
    if a < 1:
        print(-1)
        sys.exit()

answer = 0

while True:
    check()
    
