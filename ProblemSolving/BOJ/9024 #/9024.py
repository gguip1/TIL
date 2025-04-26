import sys

t = int(sys.stdin.readline().rstrip())

def solve(n:int, K:int, S:list):
    S.sort()
    left = 0
    right = n - 1
    # min_diff = (10 ** 8)
    min_diff = float('inf')
    count = 0
    
    while left < right:
        current_sum = S[left] + S[right]
        diff = abs(K - current_sum)
        
        if diff < min_diff:
            min_diff = diff
            count = 1
        elif diff == min_diff:
            count += 1
        
        if current_sum < K:
            left += 1
        else:
            right -= 1
            
    
    return count

for _ in range(t):
    n, K = map(int, sys.stdin.readline().rstrip().split())
    S = list(map(int, sys.stdin.readline().rstrip().split()))
    
    print(solve(n, K, S))
