import sys
input = sys.stdin.readline

K, L, N = map(int, input().split())
ns = input().strip()
ns += '0' * (20000 - len(ns))

current_time = 0
human_in = 0
human_out = 0
using = False

flush = []

for n in ns:
    current_time += 1
    if n == '0':
        human_out += 1
        human_in = 0

    if n == '1':
        human_in += 1
        human_out = 0
    
    if human_in >= K:
        using = True
    
    if human_out >= L:
        if using:
            flush.append(current_time)
        using = False

if flush:
    for f in flush:
        print(f)
else:
    print('NIKAD')
