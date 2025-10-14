import sys
input = sys.stdin.readline

N = int(input())
days = []

for _ in range(N):
    exciting_day = int(input())
    
    if exciting_day == 1:
        continue
    
    add_day = True
    
    for day in days:
        if (exciting_day - 1) % day == 0:
            add_day = False
    
    if add_day:
        days.append(exciting_day - 1)

print(len(days))
