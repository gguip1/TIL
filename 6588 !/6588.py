import sys

MAX = 1000000

prime_list = [1 for x in range(MAX + 1)]

for i in range(0, int(MAX ** 0.5) + 1):
    if i == 0 or i == 1:
        prime_list[i] = 0
        continue
    
    if prime_list[i] == 1:
        for j in range(i * i, MAX + 1, i):
            prime_list[j] = 0
        
input = sys.stdin.readline

while True:
    Q = int(input().strip())
    
    if Q == 0:
        break
    
    for i in range(Q + 1):
        if prime_list[i] == 1 and prime_list[Q - i] == 1:
            print(f'{Q} = {i} + {Q - i}')
            break
