# import sys
# from itertools import combinations

# input = sys.stdin.readline

# N, M = map(int, input().split())
# map_input = [list(map(int, input().split())) for _ in range(N)]

# def calc_distance(r1, c1, r2, c2):
#     return abs(r1 - r2) + abs(c1 - c2)

# home_positions = []
# chicken_poisitons = []

# for y in range(N):
#     for x in range(N):
#         if map_input[y][x] == 1:
#             home_positions.append((y, x))
#         if map_input[y][x] == 2:
#             chicken_poisitons.append((y, x))

# def solve(chicken_positions:tuple):
#     distances = []
#     for home_y, home_x in home_positions:
#         min_distane = float('inf')
#         for chicken_y, chicken_x in chicken_positions:
#             min_distane = min(calc_distance(home_y, home_x, chicken_y, chicken_x), min_distane)
#         distances.append(min_distane)
#     return distances

# answer = float('inf')

# for combo in combinations(chicken_poisitons, M):
#     answer = min(sum(solve(combo)), answer)

# print(answer)

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
map_input = [list(map(int, input().split())) for _ in range(N)]

def calc_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

home_positions = []
chicken_poisitons = []

for y in range(N):
    for x in range(N):
        if map_input[y][x] == 1:
            home_positions.append((y, x))
        if map_input[y][x] == 2:
            chicken_poisitons.append((y, x))

answer = float('inf')

def solve(chicken_positions:tuple):
    total_distance = 0
    for home_y, home_x in home_positions:
        min_distane = float('inf')
        for chicken_y, chicken_x in chicken_positions:
            min_distane = min(calc_distance(home_y, home_x, chicken_y, chicken_x), min_distane)
        total_distance += min_distane
        if total_distance > answer:
            return float('inf')
    return total_distance

for combo in combinations(chicken_poisitons, M):
    answer = min(solve(combo), answer)

print(answer)
