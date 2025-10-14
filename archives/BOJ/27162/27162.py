import sys
input = sys.stdin.readline

yachts = list(input().strip())
fixed = list(map(int, input().split()))
answer = 0

## nums_check [0 ~ 5]
def check_nums(target_num):
    answer = 0
    for i in range(3):
        if fixed[i] == target_num:
            answer += target_num
    return answer + target_num * 2

for i in range(6):
    if yachts[i] == 'Y':
        answer = max(answer, check_nums(i + 1))

## fixed count
fixed_count = [0] * 6
for i in range(3):
    fixed_count[fixed[i] - 1] += 1

## four_card_check [6]
def check_four_card():
    for i in range(6):
        if fixed_count[i] >= 2:
            return (i + 1) * 4
    return 0

if yachts[6] == 'Y':
    answer = max(answer, check_four_card())

## full_house_check [7]
def check_full_house():
    has_one = 0
    has_two = 0
    has_three = 0
    for i in range(6):
        if fixed_count[i] == 1:
            has_one = i + 1
        if fixed_count[i] == 2:
            has_two = i + 1
        if fixed_count[i] == 3:
            has_three = i + 1
    if has_one > 0 and has_two > 0:
        if has_one > has_two:
            return has_one * 3 + has_two * 2
        elif has_two > has_one:
            return has_one * 2 + has_two * 3
    if has_three > 0:
        if has_three == 6:
            return has_three * 3 + 10
        else:
            return has_three * 3 + 12
    return 0

if yachts[7] == 'Y':
    answer = max(answer, check_full_house())

## straights [8 ~ 9]
def check_little_straight():
    has_one_length = 0
    for i in range(6):
        if fixed_count[i] == 1:
            has_one_length += 1
    if has_one_length == 3:
        if 6 not in fixed:
            return 30
    return 0

def check_big_straight():
    has_one_length = 0
    for i in range(6):
        if fixed_count[i] == 1:
            has_one_length += 1
    if has_one_length == 3:
        if 1 not in fixed:
            return 30
    return 0

if yachts[8] == 'Y':
    answer = max(answer, check_little_straight())
    
if yachts[9] == 'Y':
    answer = max(answer, check_big_straight())

## yacht [10]
def check_yacht():
    for i in range(6):
        if fixed_count[i] == 3:
            return 50
    return 0

if yachts[10] == 'Y':
    answer = max(answer, check_yacht())

## choice [11]
if yachts[11] == 'Y':
    answer = max(answer, sum(fixed) + 12)

print(answer)