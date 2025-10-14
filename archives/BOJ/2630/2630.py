def checkColor(matrix, color):
    for l in matrix:
        for u in l:
            if u != color:
                return False
    
    return True

def dac(matrix):
    if checkColor(matrix, 0):
        return (1, 0)
    elif checkColor(matrix, 1):
        return (0, 1)
    
    mid = len(matrix) // 2
    
    q1 = [m[:mid] for m in matrix[:mid]]
    q2 = [m[mid:] for m in matrix[:mid]]
    q3 = [m[:mid] for m in matrix[mid:]]
    q4 = [m[mid:] for m in matrix[mid:]]
    
    w1, b1 = dac(q1)
    w2, b2 = dac(q2)
    w3, b3 = dac(q3)
    w4, b4 = dac(q4)
    
    return (w1 + w2 + w3 + w4, b1 + b2 + b3 + b4)

import sys

N = int(sys.stdin.readline().rstrip())

matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for x in range(N)]

white, blue = dac(matrix)

print(white)
print(blue)