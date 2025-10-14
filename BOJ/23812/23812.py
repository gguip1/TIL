N = int(input())

base = [[True, False, False, False, True],
        [True, True, True, True, True],
        [True, False, False, False, True],
        [True, True, True, True, True],
        [True, False, False, False, True]]

for cell in base:
    for y in range(N):
        for c in cell:
            for x in range(N):
                if c:
                    print('@', end='')
                else:
                    print(' ', end='')
        print()