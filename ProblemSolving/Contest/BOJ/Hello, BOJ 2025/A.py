import sys

X = int(sys.stdin.readline().strip())

while True:
    X += 1
    if len(str(X)) != 4:
        X = -1
        break
    first = str(X)[:2]
    second = str(X)[2:]
    
    if ((int(first) + int(second)) ** 2) == X:
        break

print(X)