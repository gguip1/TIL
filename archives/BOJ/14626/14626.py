import sys
input = sys.stdin.readline
ISBN = input().strip()

calc_value = 0
one = False

for index, value in enumerate(ISBN):
    if value == "*":
        if index % 2 == 0:
            one = True
    else:
        if index % 2 == 0:
            calc_value += int(value)
        else:
            calc_value += int(value) * 3

if one:
    for i in range(10):
        if (calc_value + i) % 10 == 0:
            print(i)
else:
    for i in range(10):
        if (calc_value + i * 3) % 10 == 0:
            print(i)