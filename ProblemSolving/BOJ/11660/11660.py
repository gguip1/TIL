import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

ranges = []
for _ in range(M):
    ranges.append(list(map(int, sys.stdin.readline().rstrip().split())))

prefixSum = [[0 for x in range(N)] for y in range(N)]
for y in range(N):
    for x in range(N):
        if y == 0 and x == 0:
            prefixSum[y][x] = matrix[y][x]
        elif y == 0 and x != 0:
            prefixSum[y][x] = matrix[y][x] + prefixSum[y][x] + prefixSum[y][x - 1]
        elif y != 0 and x == 0:
            prefixSum[y][x] = matrix[y][x] + prefixSum[y - 1][x] + prefixSum[y][x]
        else:
            prefixSum[y][x] = matrix[y][x] + prefixSum[y - 1][x] + prefixSum[y][x - 1] - prefixSum[y - 1][x - 1]

# print('------------')
# for ps in prefixSum:
#     print(*ps)
# print('------------')

for r in ranges:
    start_y, start_x, end_y, end_x = r
    start_y -= 1
    start_x -= 1
    end_y -= 1
    end_x -= 1
    
    if start_y == 0 and start_x == 0:
        print(prefixSum[end_y][end_x])
    elif start_y == 0 and start_x != 0:
        print(prefixSum[end_y][end_x] - prefixSum[end_y][start_x - 1])
    elif start_y != 0 and start_x == 0:
        print(prefixSum[end_y][end_x] - prefixSum[start_y - 1][end_x])
    else:
        print(prefixSum[end_y][end_x] - prefixSum[start_y - 1][end_x] - prefixSum[end_y][start_x - 1] + prefixSum[start_y - 1][start_x - 1])