import sys

times = int(sys.stdin.readline().rstrip())
moves = list(sys.stdin.readline().rstrip())

direction = 180

def validDirection():
    global direction
    if direction >= 360:
        direction -= 360
    elif direction < 0:
        direction += 360

records = [[0, 0]]
now = [0, 0]

for move in moves:
    if move == 'R':
        direction += 90
        validDirection()
    elif move == 'L':
        direction -= 90
        validDirection()
    elif move == 'F':
        if direction == 0:
            now[1] -= 1
        elif direction == 90:
            now[0] += 1
        elif direction == 180:
            now[1] += 1
        elif direction == 270:
            now[0] -= 1
        records.append(now.copy())

x = []
y = []

for record in records:
    x.append(record[0])
    y.append(record[1])

matrix = [['#' for x in range(max(x) + abs(min(x)) + 1)] for y in range(max(y) + abs(min(y)) + 1)]

for record in records:
    matrix[record[1] + abs(min(y))][record[0] + abs(min(x))] = '.'

for m in matrix:
    for _ in m:
        print(_, end='')
    print()