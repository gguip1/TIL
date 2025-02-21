N, r, c = map(int, input().split())

matrix = [[0 for col in range(2 ** N)] for row in range(2 ** N)]

print((2 ** N) % 2)
