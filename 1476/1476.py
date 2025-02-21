import sys

E, S, M = map(int, sys.stdin.readline().strip().split())

year = 0

while True:
    e = year % 15 + 1
    s = year % 28 + 1
    m = year % 19 + 1
    
    if E == e and S == s and M == m:
        print(year + 1)
        break
    year += 1
