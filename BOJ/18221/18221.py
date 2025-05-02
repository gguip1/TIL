import sys

N = int(sys.stdin.readline().strip())

MAP = [list(map(int, sys.stdin.readline().strip().split())) for x in range(N)]

professor = []
seonggyu = []
student = 0

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2:
            seonggyu = [i, j]
        elif MAP[i][j] == 5:
            professor = [i, j]
        if seonggyu and professor:
            break
    if seonggyu and professor:
        break

if ((abs(professor[0] - seonggyu[0]) ** 2 + abs(professor[1] - seonggyu[1]) ** 2) ** 0.5) >= 5:
    if professor[0] < seonggyu[0]:
        min_x = professor[0]
        max_x = seonggyu[0]
    else:
        min_x = seonggyu[0]
        max_x = professor[0]
    
    if professor[1] < seonggyu[1]:
        min_y = professor[1]
        max_y = seonggyu[1]
    else:
        min_y = seonggyu[1]
        max_y = professor[1]
    
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if MAP[i][j] == 1:
                student += 1
    
    if student >= 3:
        print(1)
    else:
        print(0)
    
else:
    print(0)
