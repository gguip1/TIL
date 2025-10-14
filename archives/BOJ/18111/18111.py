# python3에서 시간 초과, pypy 통과

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
grounds = [list(map(int, input().split())) for _ in range(N)]

min_time = float('inf')
height = 0

max_height = 256

while max_height >= 0:
    time = 0
    blocks = B

    for y in range(N):
        for x in range(M):
            if grounds[y][x] > max_height:
                time += (grounds[y][x] - max_height) * 2
                blocks += grounds[y][x] - max_height
            else:
                time += max_height - grounds[y][x]
                blocks -= max_height - grounds[y][x]
    
    if blocks >= 0:
        if time < min_time:
            min_time = min(time, min_time)
            height = max_height
    
    max_height -= 1

print(min_time, height)
