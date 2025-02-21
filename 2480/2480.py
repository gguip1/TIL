import sys

first_dice, second_dice, third_dice = map(int, sys.stdin.readline().strip().split())

if first_dice == second_dice == third_dice:
    print(10000 + first_dice * 1000)
elif first_dice != second_dice and second_dice != third_dice and first_dice != third_dice:
    print(max(first_dice, second_dice, third_dice) * 100)
else:
    if first_dice == second_dice:
        print(1000 + first_dice * 100)
    elif second_dice == third_dice:
        print(1000 + second_dice * 100)
    elif first_dice == third_dice:
        print(1000 + first_dice * 100)
