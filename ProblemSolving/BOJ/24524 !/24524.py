import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

dp = [0] * len(T)

for sIndex, sValue in enumerate(S):
    for tIndex, tValue in enumerate(T):
        if sValue == tValue:
            if tIndex == 0 or dp[tIndex - 1] > dp[tIndex]:
                dp[tIndex] += 1

print(dp[-1])

## 시간 초과

# result = 0

# while True:
#     popIndex = []
#     checkIndex = -1
#     for tIndex, tValue in enumerate(T):
#         for sIndex, sValue in enumerate(S):
#             if len(popIndex) > 0 and sIndex <= popIndex[len(popIndex) - 1]:
#                 continue
#             if tValue == sValue:
#                 popIndex.append(sIndex)
#                 checkIndex = sIndex
#                 break
#     if len(popIndex) == len(T):
#         result += 1
#         for index, pop in enumerate(popIndex):
#             S.pop(pop - index)
#     else:
#         break

# print(result)