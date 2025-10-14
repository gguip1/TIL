# import sys
# N = int(sys.stdin.readline().rstrip())
# cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
# answer = 0

# print(cards)

# for index in range(N - 1):
#     if cards[index] > cards[index + 1]:
#         answer += 1

# print(answer)

import sys

arr = [0] * 1000001

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    arr[int(sys.stdin.readline().rstrip())] = i + 1

answer = 0
for i in range(N):
    if arr[i] > arr[i + 1]:
        answer += 1

print(answer)