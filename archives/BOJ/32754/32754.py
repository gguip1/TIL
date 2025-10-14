import sys

input = sys.stdin.readline

N, R = map(int, input().split())
devices = [list(map(int, input().split())) for _ in range(N)]

answer = 0

for device in devices:
    x1, y1, x2, y2, x3, y3, x4, y4 = device
    
    center = (abs(x1 + x3) / 2, abs(y1 + y3) / 2)
    
    if (center[0] ** 2 + center[1] ** 2) ** 0.5 <= R + (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2 + abs(x4 - x1) ** 2 + abs(y4 - y1) ** 2) ** 0.5 / 2:
        answer += 1

print(answer)
