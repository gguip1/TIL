import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    answer = 0
    best_value = 0
    
    for __ in range(N):
        W, C = map(int, input().split())
        if best_value < (W / C):
            answer = C
            best_value = W / C
        elif best_value == (W / C):
            answer = min(answer, C)
        
    print(answer)