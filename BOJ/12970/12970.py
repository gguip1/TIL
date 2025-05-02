import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

def string_generator(n):
    return 'B' * N

def check_string(string):
    count = 0
    for i in range(N - 1):
        for j in range(i, N):
            if string[i] == 'A' and string[j] == 'B':
                count += 1
    if count == K:
        return True
    else:
        return False

result = -1
n = N

while True:
    string = string_generator()
    string = 'B' * n
    
    if check_string(string):
        result = string
        break

print(result)