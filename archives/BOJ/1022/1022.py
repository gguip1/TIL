import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

r_sz = abs(r1) + abs(r2) + 1
c_sz = abs(c1) + abs(c2) + 1

zero_y = r_sz - r2 - 1
zero_x = c_sz - c2 - 1
paper = [[0 for _ in range(c_sz)] for _ in range(r_sz)]

y = zero_y
x = zero_x

num = 1
while True:
    paper[y][x] = num
    num += 1
    
    y += 1
    x += 1
    y -= 1
    x -= 1
    
    