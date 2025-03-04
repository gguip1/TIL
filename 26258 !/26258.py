import sys

N = int(sys.stdin.readline().strip())

coordinate = []

for i in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().strip().split())))

Q = int(sys.stdin.readline().strip())

for i in range(Q):
    k = float(sys.stdin.readline().strip())
    
    left = 0
    right = len(coordinate) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        
        if coordinate[mid][0] == k:
            result = mid
            break
        elif coordinate[mid][0] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    if result == -1:
        result = right

    if coordinate[result][1] < coordinate[result + 1][1]:
        print(1)
    elif coordinate[result][1] == coordinate[result + 1][1]:
        print(0)
    else:
        print(-1)