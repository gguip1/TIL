import sys

N, r, c = map(int, sys.stdin.readline().strip().split())

def ZConquer(size, x, y, index):
    if size == 2:
        if x == c and y == r:
            return index
        elif x + 1 == c and y == r:
            return index + 1
        elif x == c and y + 1 == r:
            return index + 2
        elif x + 1 == c and y + 1 == r:
            return index + 3
    
    mid_n = size // 2
    
    if c < x + mid_n and r < y + mid_n:
        return ZConquer(mid_n, x, y, index)
    elif c >= x + mid_n and r < y + mid_n:
        return ZConquer(mid_n, x + mid_n, y, index + 1 * (mid_n ** 2))
    elif c < x + mid_n and r >= y + mid_n:
        return ZConquer(mid_n, x, y + mid_n, index + 2 * (mid_n ** 2))
    elif c >= x + mid_n and r >= y + mid_n:
        return ZConquer(mid_n, x + mid_n, y + mid_n, index + 3 * (mid_n ** 2))

print(ZConquer(2 ** N, 0, 0, 0))

# O = [[0] * (2 ** N) for x in range(2 ** N)]

# def ZConquer(N, O, x, y, index):
#     if N == 2:
#         O[x][y] = index
#         O[x][y + 1] = index + 1
#         O[x + 1][y] = index + 2
#         O[x + 1][y + 1] = index + 3
#         index += 4
#         return index
    
#     mid_n = N // 2
    
#     index = ZConquer(mid_n, O, x, y, index)
#     index = ZConquer(mid_n, O, x, y + mid_n, index)
#     index = ZConquer(mid_n, O, x + mid_n, y, index)
#     index = ZConquer(mid_n, O, x + mid_n, y + mid_n, index)
    
#     return index


# ZConquer(2 ** N, O, 0, 0, 0)

# print(O[r][c])

