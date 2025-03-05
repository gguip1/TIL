import sys

N = int(sys.stdin.readline().strip())

'''Case D '''
time = [list(map(int, sys.stdin.readline().strip().split())) for x in range(N)]
time.sort(key=lambda t:(t[1],t[0]))

count = 0
now_time = 0

for start, end in time:
    if start >= now_time:
        count += 1
        now_time = end

print(count)

# '''Case C : 실패'''
# time = [list(map(int, sys.stdin.readline().strip().split())) for x in range(N)]
# time.sort(key=lambda t:t[1])

# count = 0
# now_time = 0

# for start, end in time:
#     if start < now_time:
#         continue
#     else:
#         count += 1
#         now_time = end

# print(count)


'''Case A : 시간초과'''
# def end_sort(time):
#     length = len(time) - 1
#     for i in range(length):
#         for j in range(length - i):
#             if (time[j][1] > time[j + 1][1]):
#                 time[j][1], time[j + 1][1] = time[j + 1][1], time[j][1]
#     return time

# time = end_sort([list(map(int, sys.stdin.readline().strip().split())) for x in range(N)])

# max_count = 0
# for index, value in enumerate(time[:-1]):
#     time_table = []
#     time_table.append(value)
#     for i,v in enumerate(time[index + 1:]):
#         if v[0] < time_table[-1][1]:
#             continue
#         else:
#             time_table.append(v)
    
#     max_count = max(max_count, len(time_table))

# print(max_count)

'''Case B : 시간초과'''
# time = [list(map(int, sys.stdin.readline().strip().split())) for x in range(N)]

# max_count = 0

# for index, value in enumerate(time[:-1]):
#     time_table = []
#     time_table.append(value)
#     for i, v in enumerate(time[index + 1:]):
#         if v[0] < time_table[-1][0] < v[1] or v[0] < time_table[-1][1] < v[1] or time_table[-1][0] < v[0] < time_table[-1][1] or time_table[-1][0] < v[1] < time_table[-1][1]:
#             continue
#         else:
#             time_table.append(v)

#     if len(time_table) == 5:
#         print(time_table)
#     max_count = max(max_count, len(time_table))
    
# print(max_count)
