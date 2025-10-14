import sys

N = int(sys.stdin.readline().rstrip())

result = [[0] * N for _ in range(2)]

left = N - 1
right = 0
j = 1

for i in range(N):
    if left == right:
        result[0][left] = N
        result[1][j - 1] = left + 1
        break
    
    if i % 2 == 0:
        result[0][left] = N - j
        result[1][j - 1] = left + 1
        left -= 1
    else:
        result[0][right] = N - j
        result[1][j - 1] = right + 1
        right += 1
    
    j += 1

print('YES')
print(*result[0])
print(*result[1])
