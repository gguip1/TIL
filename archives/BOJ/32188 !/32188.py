from collections import deque
import sys
input = sys.stdin.readline

N, C = map(int, input().split())

line = [-1] * N
portals = dict()

for _ in range(C):
    _portal, _from, _to = map(int, input().split())
    line[_from] = _portal
    portals[_from] = _to

queue = deque([0])
times = [float('inf')] * N
times[0] = 0

while queue:
    _position = queue.popleft()
    _time = times[_position]
    
    if _position == N - 1:
        continue
    
    if _position + 1 < N and times[_position + 1] > _time + 1:
        if line[_position] in (-1, 1):
            times[_position + 1] = _time + 1
            queue.append(_position + 1)
    
    if line[_position] in (0, 1):
        if portals[_position] < N and times[portals[_position]] > _time:
            times[portals[_position]] = _time
            queue.appendleft(portals[_position])

print(-1 if times[N - 1] == float('inf') else times[N - 1])