import sys

t = int(sys.stdin.readline())

def get_fibo():
    fibo = [1, 2]
    
    x = 0
    y = 1
    
    while fibo[x] + fibo[y] < 25000:
        fibo.append(fibo[x] + fibo[y])
        x += 1
        y += 1
    
    return fibo

def solve(x):
    fibo = get_fibo()
    indexes = []
    
    while x != 0:
        index = 0
        while index < 21 and fibo[index] <= x:
            index += 1
        index -= 1
        x -= fibo[index]
        indexes.append(index)
    
    result = 0
    for index in indexes:
        index -= 1
        if index >= 0:
            result += fibo[index]
    
    return result

for i in range(t):
    x = int(sys.stdin.readline())
    print(solve(x))