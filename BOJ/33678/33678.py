import sys
from collections import deque

N, K, X = map(int, sys.stdin.readline().rstrip().split())
wages = list(map(int, sys.stdin.readline().rstrip().split()))

vacation = 0

pre_vacation = deque()
post_vacation = deque()

for index in range(N)):
    if index == 0:
        pre_vacation.append(wages[index] * X)
    else:
        pre_vacation.append(pre_vacation[index - 1] + wages[index] * X)

for index in range(N - 1, -1, -1):
    if index == N - 1:
        post_vacation.append(wages[index])
    else:
        post_vacation.appendleft(post_vacation[0] + wages[index])

for left in range(N):
    right = N - left - 1
    
    if pre_vacation[left] >= K:
        vacation = N - (left + 1)
        break
    
    if post_vacation[right] >= K:
        vacation = N - (left + 1)
        break

if vacation <= 0:
    print(-1)
else:
    print(vacation)