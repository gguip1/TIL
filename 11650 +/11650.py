import sys

N = int(sys.stdin.readline().strip())

coordinates = [list(map(int, sys.stdin.readline().strip().split())) for x in range(N)]

# MergeSort


# # 시간 초과 BubbleSort
# for i in range(N - 1):
#     for j in range(N - i - 1):
#         if coordinates[j][0] > coordinates[j + 1][0]:
#             coordinates[j], coordinates[j + 1] = coordinates[j + 1], coordinates[j]
#         elif coordinates[j][0] == coordinates[j + 1][0]:
#             if coordinates[j][1] > coordinates[j + 1][1]:
#                 coordinates[j], coordinates[j + 1] = coordinates[j + 1], coordinates[j]

# for coordinate in coordinates:
#     print(coordinate[0], coordinate[1])

# # 이건 좀...
# coordinates.sort()

# for coordinate in coordinates:
#     print(coordinate[0], coordinate[1])
