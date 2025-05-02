import sys

def factorial(num):
    result = 1
    for i in range(num):
        result *= (i + 1)
    return result

N, K = map(int, sys.stdin.readline().strip().split())

print(int(factorial(N) / (factorial(K) * factorial(N - K))))
