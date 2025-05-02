import sys

N = int(sys.stdin.readline().rstrip())

matrices = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
result = 0

while len(matrices) > 1:
    row0, column0 = matrices[len(matrices) - 2]
    row1, column1 = matrices[len(matrices) - 1]
    
    result += (row0 * column0 * column1)
    
    matrices.pop()
    matrices.pop()
    matrices.append((row0, column1))

print(result)

# while len(matrices) > 1:
#     minIndex = 0
#     checkValue = None
    
#     for index in range(len(matrices) - 1):
#         r0, c0 = matrices[index]
#         r1, c1 = matrices[index + 1]
#         value = r0 * c0 * c1
#         if checkValue is None or checkValue > value:
#             checkValue = value
#             minIndex = index
    
#     row0, column0 = matrices[minIndex]
#     row1, column1 = matrices[minIndex + 1]
    
#     result += (row0 * column0 * column1)    
    
#     matrices.pop(minIndex)
#     matrices.pop(minIndex)
#     matrices.insert(minIndex, (row0, column1))