import sys

N = int(sys.stdin.readline().strip())

result = 0
for i in range(1, N + 1):
    result += (N // i) * i

print(result)

# # 시간 초과
# def func_f(num):
#     result = 0
#     for i in range(1, int((num + 1) ** 0.5) + 1):
#         if num % i == 0:
#             result += i
#             if i != num // i:
#                 result += num // i
#     return result

# def func_s(num):
#     result = 0
#     for i in range(1, num + 1):
#         result += func_f(i)
#     return result

# print(func_s(N))
