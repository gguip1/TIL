T = int(input())

result = []

def factorial(num):
    
    result = 1
    
    for i in range(num):
        
        result *= i + 1
    
    return result

for i in range(T):

    N, M = map(int, input().split())

    result.append(int(factorial(M) / (factorial(M - N) * factorial(N))))

for index, value in enumerate(result):
    
    print(value)
