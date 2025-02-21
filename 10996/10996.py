N = int(input())

for i in range(N * 2):
    if i % 2 == 0:
        for j in range(N):
            if j % 2 == 0:
                print('*', end='')
            else:
                print(end=' ')
    else:
        for j in range(N):
            if j % 2 == 0:
                print(end=' ')
            else:
                print('*', end='')
    print()
