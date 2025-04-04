import sys

while True:
    N = int(sys.stdin.readline().rstrip())
    
    if N == 0:
        break
    
    prices = [price for price in range(2, N + 2)]
    
    count = 0
    
    for i in range(N):
        amount = 0
        for j in range(i, N):
            amount += prices[j]
            if amount == N:
                count += 1
                break
            elif amount > N:
                break
    
    print(count)