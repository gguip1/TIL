import sys

num_arr = [0 for _ in range(53)]

N = int(sys.stdin.readline().strip())

for q in list(map(int, sys.stdin.readline().strip().split())):
    num_arr[q] += 1

for q in list(sys.stdin.readline().strip()):
    if q == ' ':
        num_arr[0] -= 1
    elif (ord(q) - 64) <= 26:
        num_arr[ord(q) - 64] -= 1
    else:
        num_arr[ord(q)- 70] -= 1

result = True

for n in num_arr:
    if n != 0:
        result = False
        break

if result:
    print('y')
else:
    print('n')