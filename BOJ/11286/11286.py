import sys
input = sys.stdin.readline

N = int(input())

### TLE
# array = []

# for i in range(N):
#     x = int(input())
    
#     if x == 0:
#         if array:
#             print(array.pop()[1])
#         else:
#             print(0)
#     else:
#         array.append((abs(x), x))
#         array.sort(reverse=True)

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
        heapq.heappush(array, (abs(x), x))
