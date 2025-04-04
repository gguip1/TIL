from collections import deque

import sys

N, L = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

window = deque()
D = []

for i in range(N):
    if window and window[0] == i - L:
        window.popleft()
    
    while window and A[window[-1]] > A[i]:
        window.pop()
    
    window.append(i)
    
    D.append(A[window[0]])

print(*D)
