def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    K = int(sys.stdin.readline().rstrip())
    
    primes = []
    
    for j in range(2, K):
        if isPrime(j):
            primes.append(j)
    
    result = []
    
    for i in primes:
        for j in primes:
            for z in primes:
                if K == i + j + z:
                    result.append(i)
                    result.append(j)
                    result.append(z)
                if len(result) == 3:
                    break
            if len(result) == 3:
                break
        if len(result) == 3:
                    break
    if len(result) == 0:
        print(0)
    else:
        print(*result)
    
