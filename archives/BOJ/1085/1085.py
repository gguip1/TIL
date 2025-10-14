import sys

x, y, w, h = map(int, sys.stdin.readline().strip().split())

near_x = abs(x - w) if abs(x - w) < x else x
near_y = abs(y - h) if abs(y - h) < y else y

print(near_x if near_x < near_y else near_y)
