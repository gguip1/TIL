import sys

S = sys.stdin.readline().strip()

amount = 0
count = 0

for s in S:
    
    if s == 'A':
        amount += 4
    elif s == 'B':
        amount += 3
    elif s == 'C':
        amount += 2
    elif s == 'D':
        amount += 1
    elif s == 'F':
        amount += 0
    elif s == '+':
        amount += 0.5
        continue
    
    count += 1

print(round(amount / count, 5))
