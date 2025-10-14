import sys

now = 100

target = int(sys.stdin.readline().strip())
break_button_n = int(sys.stdin.readline().strip())
break_buttons = sys.stdin.readline().strip().split()

min_count = abs(target - now)

for num in range(999999):
    num = str(num)

    check = True
    
    for n in num:
        if n in break_buttons:
            check = False
            break
    
    if check:
        min_count = min(min_count, abs(target - int(num)) + len(num))

print(min_count)
