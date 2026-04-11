import sys
input = sys.stdin.readline

N = int(input())

paper = [[False] * 100 for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())

    for y in range(99 - b, 99 - 10 - b, -1):
        for x in range(a, a + 10):
            if 0 <= y and y < 100 and 0 <= x and x < 100:
                paper[y][x] = True

count = 0

for y in range(100):
    for x in range(100):    
        if paper[y][x]:
            count += 1

print(count)
