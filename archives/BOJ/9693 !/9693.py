import sys

result = [0 for _ in range(1000001)]

for x in range(5, 1000001):
    result[x] = result[x - 1]
    
    for i in range(1, 9):
        if x % (5 ** i) == 0:
            result[x] += 1

index = 0
while True:
    index += 1
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break
    print(f'Case #{index}: {result[N]}')

