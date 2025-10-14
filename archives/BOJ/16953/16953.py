import sys

A, B = map(int, sys.stdin.readline().strip().split())

queue = [(A, 1)]
visited = set()
answer = -1

while queue:
    val, cnt = queue.pop(0)
    
    if val == B:
        answer = cnt
        break
    
    if val <= B and val not in visited:
        visited.add(val)
        queue.append((val * 2, cnt + 1))
        queue.append((int(str(val) + '1'), cnt + 1))

print(answer)