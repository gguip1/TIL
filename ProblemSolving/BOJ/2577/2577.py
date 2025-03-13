import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

result = str(A * B * C)

output = [0 for x in range(10)]

for i in range(len(result)):
    for j in range(10):
        if result[i] == str(j):
            output[j] += 1

for o in output:
    print(o)
