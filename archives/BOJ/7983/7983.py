import sys

n = int(sys.stdin.readline().rstrip())
homeworks = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

homeworks.sort(key=lambda homework: homework[1], reverse=True)

now = None

for homework in homeworks:
    d, t = homework
    
    if now is None or now > t:
        now = t - d + 1
        continue
    
    now -= d

if now < 1:
    print(0)
else:
    print(now - 1)
