import sys

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_list = [0 for x in range(1000001)]

for i in range(2, 1000001):
    if is_prime(i):
        prime_list[i] = 1

input = sys.stdin.readline

while True:
    Q = int(input().strip())
    
    if Q == 0:
        break
    
    for i in range(Q + 1):
        if prime_list[i] == 1 and prime_list[Q - i] == 1:
            print(f'{Q} = {i} + {Q - i}')
            break

