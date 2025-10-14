import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
LANS = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

left = 1
right = max(LANS)
result = 0

while left <= right:
    mid = (right + left) // 2
    
    count = 0
    for LAN in LANS:
        count += LAN // mid
    
    if count >= N:
        result = mid
        left = mid + 1
    elif count < N:
        right = mid - 1

print(result)