import sys

N = int(sys.stdin.readline().strip())
P = list(map(int, sys.stdin.readline().strip().split()))

P_price = [(p / (i + 1)) for i, p in enumerate(P)]

while N != 0:
    max_index, mav_value = -1, -1
    for index, value in enumerate(P_price):
        max_index = max(max_index, index)
        max_value = max(max_value, value)
    