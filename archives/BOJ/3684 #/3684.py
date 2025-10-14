import sys

T = int(sys.stdin.readline().strip())

x_input = [int(sys.stdin.readline().strip()) for x in range(T)]

# # pypy
# flag = False

# a_value = 0
# b_value = 0

# for a in range(10001):
#     for b in range(10001):
#         count = 0
#         for i in range(T - 1):
#             if (a * ((a * x_input[i] + b) % 10001) + b) % 10001 == x_input[i + 1]:
#                 count += 1
#             else:
#                 break
#         if count == (T - 1):
#             flag = True
#             a_value = a
#             b_value = b
#         if flag:
#             break
#     if flag:
#         break

# for x in x_input:
#     print((a_value * x + b_value) % 10001)
