import sys
input = sys.stdin.readline

matrix = [list(map(int, input().split())) for _ in range(9)]

max_value = -1
row_index = 0
column_index = 0

for r in range(9):
    for c in range(9):
        if matrix[r][c] > max_value:
            max_value = matrix[r][c]
            row_index = r + 1
            column_index = c + 1

print(max_value)
print(row_index, column_index)
