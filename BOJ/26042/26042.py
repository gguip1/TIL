import sys
input = sys.stdin.readline

n = int(input())
queue = []
max_count = 0
max_last = 0

for _ in range(n):
    a = list(map(int, input().split()))

    if len(a) == 2:
        queue.append(a[1])
    else:
        queue.pop(0)
    
    if max_count < len(queue):
        max_count = len(queue)
        max_last = queue[-1]
    elif max_count == len(queue):
        max_last = min(max_last, queue[-1])

print(max_count, max_last)