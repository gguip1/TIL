N = int(input())

def factorial(num):
    if num > 1:
        return factorial(num - 1) * num
    else:
        return 1

N_list = list(str(factorial(N)))

N_list_len = len(N_list)

count = 0

for i in range(N_list_len - 1, 0, -1):
    if int(N_list[i]) != 0:
        break
    else:
        count += 1

print(count)
