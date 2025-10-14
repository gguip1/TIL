import sys
input = sys.stdin.readline
N = int(input())

import heapq

array = []

for i in range(N):
    x = int(input())
    
    if x == 0:
        if array:
            print(heapq.heappop(array)[1])
        else:
            print(0)
    else:
        heapq.heappush(array, (2 ** 31 - x, x))
    