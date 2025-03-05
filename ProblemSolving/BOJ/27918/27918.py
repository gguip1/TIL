import sys

N = int(sys.stdin.readline().strip())

p1 = p2 = 0

Qs = []

for i in range(N):
    Qs.append(sys.stdin.readline().strip())

for Q in Qs:
    if Q == 'D':
        p1 += 1
    else:
        p2 += 1
    
    if abs(p1 - p2) >= 2:
        break

print(f'{p1}:{p2}')
