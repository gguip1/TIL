from collections import deque
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [[0] * 19 for _ in range(19)]

center = 19 // 2

for y in range(19):
    for x in range(19):
        dist = max(abs(x - center), abs(y - center))
        board[y][x] = max(10 - dist, 1)

target = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

windows = deque()

for j in range(N):
    windows.append(deque())
    for i in range(M):
        windows[j].append(target[j][i])
    print(windows)

# if N < 10 and M < 10:
#     print(-1)
#     sys.exit(0)

# for j in range(-18, N):
#     for i in range(-18, M):
#         score = [0] * 10
#         for y in range(19):
#             for x in range(19):
#                 if 0 <= j + y < N and 0 <= i + x < M:
#                     if target[j + y][i + x] == 1:
#                         score[board[y][x] - 1] += 1

#                         if board[y][x] == 10:
#                             center = (j + y, i + x)
        
#         check = True
#         for s in score:
#             if s != 1:
#                 check = False
#         if check:
#             center_y, center_x = center
#             print(center_y, center_x)
#             sys.exit(0)

# print(-1)