import sys

N, T = map(int, sys.stdin.readline().strip().split())

x, y = 0, 0

now = 0
degree = 0

for i in range(N):
    t, s = sys.stdin.readline().strip().split()
    
    if (degree % 360) == 0:
        x += (int(t) - now)
    elif (degree % 360) == 90:
        y -= (int(t) - now)
    elif (degree % 360) == 180:
        x -= (int(t) - now)
    elif (degree % 360) == 270:
        y += (int(t) - now)
    
    now = int(t)
    
    if s == 'right':
        degree += 90
    elif s == 'left':
        if degree == 0:
            degree = 270
        else:
            degree -= 90

if (degree % 360) == 0:
    x += (T - now)
elif (degree % 360) == 90:
    y -= (T - now)
elif (degree % 360) == 180:
    x -= (T - now)
elif (degree % 360) == 270:
    y += (T - now)

print(x, y)
