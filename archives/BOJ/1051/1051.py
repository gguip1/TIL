import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

rectangle = [
    list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)
]

def check_square(y, x):
    vertex = rectangle[y][x]
    remain_y = N - y
    remain_x = M - x
    
    max_side = 0
    
    for side in range(min(remain_y, remain_x)):
        delta = ((side, 0), (0, side), (side, side))

        count = 0
        
        for d in delta:
            dy, dx = d
            if rectangle[y + dy][x + dx] == vertex:
                count += 1
        
        if count == 3:
            max_side = max(max_side, side + 1)
        
    return max_side

max_side = 0

for n in range(N):
    for m in range(M):
        max_side = max(max_side, check_square(n, m))
        
print(max_side ** 2)