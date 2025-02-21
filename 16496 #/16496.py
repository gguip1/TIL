import sys

N = int(sys.stdin.readline().strip())

for _ in range(N):
    nums = list(sys.stdin.readline().split())

    result = []

    for num in nums:
        
        if len(result) == 0:
            result.append(num)
    
