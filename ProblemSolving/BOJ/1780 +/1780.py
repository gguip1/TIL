import sys

def check(matrix: list, target: int):
    for mat in matrix:
        for m in mat:
            if m != target:
                return False
    return True

def dac(matrix: list):
    if check(matrix, -1):
        return (1, 0, 0)
    elif check(matrix, 0):
        return (0, 1, 0)
    elif check(matrix, 1):
        return (0, 0, 1)
    
    div = len(matrix) // 3
    
    q1 = [mat[:div] for mat in matrix[:div]]
    q2 = [mat[div:2*div] for mat in matrix[:div]]
    q3 = [mat[2*div:] for mat in matrix[:div]]
    q4 = [mat[:div] for mat in matrix[div:2*div]]
    q5 = [mat[div:2*div] for mat in matrix[div:2*div]]
    q6 = [mat[2*div:] for mat in matrix[div:2*div]]
    q7 = [mat[:div] for mat in matrix[2*div:]]
    q8 = [mat[div:2*div] for mat in matrix[2*div:]]
    q9 = [mat[2*div:] for mat in matrix[2*div:]]
    
    a1, b1, c1 = dac(q1)
    a2, b2, c2 = dac(q2)
    a3, b3, c3 = dac(q3)
    a4, b4, c4 = dac(q4)
    a5, b5, c5 = dac(q5)
    a6, b6, c6 = dac(q6)
    a7, b7, c7 = dac(q7)
    a8, b8, c8 = dac(q8)
    a9, b9, c9 = dac(q9)
    
    return (a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9, b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9, c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9)


N = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

a, b, c = dac(matrix)

print(a)
print(b)
print(c)
