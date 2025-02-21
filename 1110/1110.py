import sys

def func(num):
    if int(num) < 10:
        num = '0' + str(int(num))
    
    new_num = str(int(num[0]) + int(num[1]))
    
    return num[len(num) - 1] + new_num[len(new_num) - 1]

N = sys.stdin.readline().strip()

N_copy = N

count = 0

while True:
    N = func(N)

    count += 1
    
    if int(N) == int(N_copy):
        break

print(count)
