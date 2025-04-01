import sys
import copy

N = int(sys.stdin.readline().rstrip())

energies = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N - 1)]
K = int(sys.stdin.readline().rstrip())

dp = [0] * N

if N == 1:
    print(0)
elif N == 2:
    print(energies[0][0])
else:
    dp[1] = energies[0][0]
    dp[2] = min(energies[0][0] + energies[1][0], energies[1][1])
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + energies[i - 1][0], dp[i - 2] +  energies[i - 2][1])
    
    result = dp[-1]
    
    checkDP = copy.deepcopy(dp)
    
    for i in range(3, N):
        checkDP[i] = K + dp[i - 3]
        
        for j in range(i + 1, N):
            checkDP[j] = min(checkDP[j - 1] + energies[j - 1][0], checkDP[j - 2] +  energies[j - 2][1])
        
        if result > checkDP[-1]:
            result = checkDP[-1]
            
    print(result)
