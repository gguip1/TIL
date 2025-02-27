import sys

hour_degree, minute_degree = map(float, sys.stdin.readline().strip().split())

hour_per_minute = 0.5

hour = hour_degree / 30
minute = minute_degree / 6

if hour_degree == (hour * (30)) + (minute * hour_per_minute):
    print("O")
else:
    print("X")

if (hour_degree % 30) * 12 == minute_degree:
    print("O")
else:
    print("X")
