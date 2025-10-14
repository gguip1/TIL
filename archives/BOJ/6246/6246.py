N, Q = map(int, input().split())

line = [0 for _ in range(N)]

for _ in range(Q):
    start, interval = map(int, input().split())
    for i in range(start - 1, N, interval):
        if line[i] == 0:
            line[i] = 1

count = 0

for l in line:
    if l == 0:
        count += 1

print(count)
