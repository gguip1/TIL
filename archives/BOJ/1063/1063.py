import sys

def char_to_num(char):
    return ord(char) - 64

def num_to_char(num):
    return chr(num + 64)

def position_to_num(position):
    position = list(position)
    return [char_to_num(position[0]), int(position[1])]

king, stone, N = sys.stdin.readline().strip().split()
king = position_to_num(king)
stone = position_to_num(stone)
N = int(N)

for _ in range(N):
    command = sys.stdin.readline().strip()

    if command == 'R' and king[0] < 8:
        if king[0] + 1 == stone[0] and king[1] == stone[1]:
            if stone[0] < 8:
                stone[0] += 1
            else:
                continue
        king[0] += 1
    elif command == 'L' and king[0] > 1:
        if king[0] - 1 == stone[0] and king[1] == stone[1]:
            if stone[0] > 1:
                stone[0] -= 1
            else:
                continue
        king[0] -= 1
    elif command == 'B' and king[1] > 1:
        if king[1] - 1 == stone[1] and king[0] == stone[0]:
            if stone[1] > 1:
                stone[1] -= 1
            else:
                continue
        king[1] -= 1
    elif command == 'T' and king[1] < 8:
        if king[1] + 1 == stone[1] and king[0] == stone[0]:
            if stone[1] < 8:
                stone[1] += 1
            else:
                continue
        king[1] += 1
    elif command == 'RT' and king[1] < 8 and king[0] < 8:
        if king[0] + 1 == stone[0] and king[1] + 1 == stone[1]:
            if stone[0] < 8 and stone[1] < 8:
                stone[0] += 1
                stone[1] += 1
            else:
                continue
        king[0] += 1
        king[1] += 1
    elif command == 'LT' and king[0] > 1 and king[1] < 8:
        if king[0] - 1 == stone[0] and king[1] + 1 == stone[1]:
            if stone[0] > 1 and stone[1] < 8:
                stone[0] -= 1
                stone[1] += 1
            else:
                continue
        king[0] -= 1
        king[1] += 1
    elif command == 'RB' and king[0] < 8 and king[1] > 1:
        if king[0] + 1 == stone[0] and king[1] - 1 == stone[1]:
            if stone[0] < 8 and stone[1] > 1:
                stone[0] += 1
                stone[1] -= 1
            else:
                continue
        king[0] += 1
        king[1] -= 1
    elif command == 'LB' and king[0] > 1 and king[1] > 1:
        if king[0] - 1 == stone[0] and king[1] - 1 == stone[1]:
            if stone[0] > 1 and stone[1] > 1:
                stone[0] -= 1
                stone[1] -= 1
            else:
                continue
        king[0] -= 1
        king[1] -= 1

for i, k in enumerate(king):
    if i == 0:
        print(num_to_char(k), end='')
    else:
        print(k)
for i, s in enumerate(stone):
    if i == 0:
        print(num_to_char(s), end='')
    else:
        print(s)