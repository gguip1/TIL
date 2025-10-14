import sys

N = int(sys.stdin.readline().rstrip())
dice = list(map(int, sys.stdin.readline().rstrip().split()))

def get_min_1(dice):
    return min(dice)

def get_min_2(dice):
    cases = [
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (1, 2),
        (2, 4),
        (4, 3),
        (3, 1),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4)
    ]
    
    values = []
    
    for case in cases:
        values.append(dice[case[0]] + dice[case[1]])
    
    return min(values)

def get_min_3(dice):
    cases = [
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 4),
        (0, 3, 4),
        (5, 1, 2),
        (5, 1, 3),
        (5, 2, 4),
        (5, 3, 4)
    ]
    
    values = []
    
    for case in cases:
        values.append(dice[case[0]] + dice[case[1]] + dice[case[2]])
    
    return min(values)

min_1 = get_min_1(dice)
min_2 = get_min_2(dice)
min_3 = get_min_3(dice)

if N == 1:
    print(sum(dice) - max(dice))
else:
    face_1 = min_1 * ((N - 2) ** 2) + min_1 * ((N - 1) * (N - 2)) * 4
    face_2 = min_2 * (N - 2) * 4 + min_2 * (N - 1) * 4
    face_3 = min_3 * 4
    print(face_1 + face_2 + face_3)