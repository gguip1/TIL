import sys

n = [int(line.strip()) for line in sys.stdin.readlines()]

for num in n:
    _ = '1'
    while True:
        if int(_) % num == 0:
            break
        _ += '1'
    print(len(_))
