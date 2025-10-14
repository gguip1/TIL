N = int(input())

check = False

for i in range(5 * N):
    if i % N == 0:
        check = not check
    
    if check:
        print('@' * 5 * N)
    else:
        print('@' * N)
