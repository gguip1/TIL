def bin(num):
    if num == 0 or num == 1:
        return str(num)
    
    return bin(num // 2) + str(num % 2)

import sys  

n, k = map(int, sys.stdin.readline().rstrip().split())

dp = []
num = 0
while len(dp) < 10001:
    for nu in list(bin(num)):
        dp.append(nu)
    num += 1

for i in range(5):
    print(dp[n * i + k - 1], end=' ')
