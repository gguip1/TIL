import sys

P, N= map(int, sys.stdin.readline().rstrip().split())
times = list(map(int, sys.stdin.readline().rstrip().split()))

times.sort()

result = 0
count = 0
check = 0

for index, time in enumerate(times):
    if check + time < P:
        result += time * (index + 1)
        check += time
        count += 1
    else:
        break

check = P - check - 1

result += count * check
print(count, result)


# for i in range(N, 0, -1):
#     checkList = times[:i]
#     checkSum = sum(checkList)
#     if checkSum < P:
#         break

# result = 0
# penality = P - checkSum - 1

# for time in reversed(checkList):
#     penality += time
#     result += penality

# print(len(checkList), result)