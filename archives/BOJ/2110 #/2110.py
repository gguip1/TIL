import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
X = [int(input().rstrip()) for _ in range(N)]

X.sort()

def binary_search():
    left = 1
    right = X[N - 1] - X[0]
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        count = 1
        prev = X[0]
        for i in range(1, N):
            if X[i] - prev >= mid:
                count += 1
                prev = X[i]
        
        if count >= C:
            result = max(result, mid)
            left = mid + 1
        else:
            right = mid - 1
        
        print(result)
    
    return result

print(binary_search())
