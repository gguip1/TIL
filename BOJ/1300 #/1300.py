import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

left = 1
right = min(10 ** 9, N ** 2)

while left <= right:
    count = 0
    mid = (left + right) // 2
    
    for i in range(1, N + 1):
        count += min(N, mid // i)
    
    if count < k:
        left = mid + 1
    else:
        right = mid - 1

print(left)