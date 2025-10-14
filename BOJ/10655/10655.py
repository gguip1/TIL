import sys
input = sys.stdin.readline

N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

_max = 0

for idx in range(N - 1):
    current_x, current_y = coordinates[idx]
    next_x, next_y = coordinates[idx + 1]
    
    _max += abs(next_x - current_x) + abs(next_y - current_y)

answer = float('inf')

for idx in range(1, N - 1):
    answer = min(answer, _max - (abs(coordinates[idx][0] - coordinates[idx - 1][0]) + abs(coordinates[idx][1] - coordinates[idx - 1][1]) + abs(coordinates[idx + 1][0] - coordinates[idx][0]) + abs(coordinates[idx + 1][1] - coordinates[idx][1])) + abs(coordinates[idx + 1][0] - coordinates[idx - 1][0]) + abs(coordinates[idx + 1][1] - coordinates[idx - 1][1]))

print(answer)
