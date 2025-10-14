import sys
input = sys.stdin.readline

N = int(input())
coordinates = list(map(int, input().split()))
coordinates_dict = {}

# prev_coordinate = None
# value = 0

# for coordinate in sorted(coordinates):
#     if coordinate == prev_coordinate:
#         continue
#     else:
#         if coordinates_dict.get(coordinate) is None:
#             coordinates_dict[coordinate] = value
#         prev_coordinate = coordinate
#         value += 1

# for coordinate in coordinates:
#     print(coordinates_dict[coordinate], end=' ')

coordinates_set = set(coordinates)

for index, value in enumerate(sorted(list(coordinates_set))):
    coordinates_dict[value] = index

for coordinate in coordinates:
    print(coordinates_dict[coordinate], end=' ')