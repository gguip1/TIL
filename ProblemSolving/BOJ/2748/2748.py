import sys

# def fibo(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fibo(num - 1) + fibo(num - 2)

# print(fibo(int(sys.stdin.readline().strip())))

n = int(sys.stdin.readline().strip())

fibo_list = [0, 1]

for i in range(2, n + 1):
    fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])

print(fibo_list[n])
