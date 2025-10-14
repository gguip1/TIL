import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

answer = 0



print(answer % (10 ** 9 + 7))

# answer = 0

# for unit in list(permutations(A, K)):
#     is_reverse = False
#     is_good = True
#     previous_element = unit[0]
#     for element in unit[1:]:
#         if is_reverse:
#             if previous_element < element:
#                 is_good = False
#                 break
#         else:
#             if previous_element > element:
#                 is_reverse = True
#         previous_element = element

#     if is_good:
#         answer += 1

# print(answer % (10 ** 9 + 7))
