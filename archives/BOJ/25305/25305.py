import sys

N, k = map(int, sys.stdin.readline().strip().split())
scores = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N - 1):
    for j in range(N - i - 1):
        if scores[j] < scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]
    
print(scores[k - 1])
