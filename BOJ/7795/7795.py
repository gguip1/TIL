import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    B.sort()
    
    answer = 0
    
    for a in A:
        left = 0
        right = M - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if B[mid] < a:
                left = mid + 1
            else:
                right = mid - 1
        
        answer += left
    
    print(answer)