import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    row, column = map(int, sys.stdin.readline().strip().split())
    
    matrix = []
    
    for r in range(row):
        matrix.append(list(sys.stdin.readline().strip().split()))

    result = 0

    for j in range(row):
        for c in range(column):
            for r in range(row):
                if r + 1 != row:
                    if matrix[r][c] == '1' and matrix[r + 1][c] == '0':
                        matrix[r][c] = '0'
                        matrix[r + 1][c] = '1'
                        result += 1
    
    print(result)
