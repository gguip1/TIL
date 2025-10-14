import sys

minute = 0
second = 0

for i in range(4):
    second += int(sys.stdin.readline())
    
while second >= 60:
    minute += 1
    second -= 60

print(minute)
print(second)
