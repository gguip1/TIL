import sys

N, M, dice_y, dice_x, K = map(int, sys.stdin.readline().rstrip().split())

map_ = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
commands = list(map(int, sys.stdin.readline().rstrip().split()))

dice = [0, 0, 0, 0, 0, 0]

answers = []

for command in commands:
    if command == 1 and dice_x + 1 < M:
        dice_x += 1
        
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp
        answers.append(dice[0])
        
        if map_[dice_y][dice_x] == 0:
            map_[dice_y][dice_x] = dice[5]
        else:
            dice[5] = map_[dice_y][dice_x]
            map_[dice_y][dice_x] = 0
        
    elif command == 2 and dice_x - 1 >= 0:
        dice_x -= 1
        
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
        answers.append(dice[0])
        
        if map_[dice_y][dice_x] == 0:
            map_[dice_y][dice_x] = dice[5]
        else:
            dice[5] = map_[dice_y][dice_x]
            map_[dice_y][dice_x] = 0
            
    elif command == 3 and dice_y - 1 >= 0:
        dice_y -= 1
        
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
        answers.append(dice[0])

        if map_[dice_y][dice_x] == 0:
            map_[dice_y][dice_x] = dice[5]
        else:
            dice[5] = map_[dice_y][dice_x]
            map_[dice_y][dice_x] = 0
        
    elif command == 4 and dice_y + 1 < N:
        dice_y += 1
        
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp
        answers.append(dice[0])
    
        if map_[dice_y][dice_x] == 0:
            map_[dice_y][dice_x] = dice[5]
        else:
            dice[5] = map_[dice_y][dice_x]
            map_[dice_y][dice_x] = 0
    
for answer in answers:
    print(answer)

