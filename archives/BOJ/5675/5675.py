import sys

degrees = []

hour = 0
minute = 0

hour_per_degree = 360 // 12
minute_per_degree = 360 // 60

while hour < 12:
    degree = abs(minute_per_degree * minute - hour_per_degree * hour)
    if degree <= 180:
        degrees.append(degree)
    else:
        degrees.append(360 - degree)
    
    minute += 1
    if minute == 60:
        minute = 0
        hour += 1

for line in sys.stdin:
    A = int(line.strip())
    
    if A in degrees:
        print('Y')
    else:
        print('N')