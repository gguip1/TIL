import sys

N = int(sys.stdin.readline().strip())

count = 0
count_list = []

while True:
    if N % 5 == 0:
        count_list.append(count + N // 5)
        
    if N % 3 == 0:
        count_list.append(count + N // 3)
    
    N -= 5
    count += 1
    
    if N < 3:
        break


if count_list:
    print(min(count_list))
else:
    print(-1)