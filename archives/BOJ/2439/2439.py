N = int(input())

for i in range(N-1, -1, -1):
    for j in range(N):
        if i <= j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
