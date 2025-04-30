import sys

N = int(sys.stdin.readline())

score = [int(sys.stdin.readline()) for _ in range(N)]

result = 0

for i in range(N - 1, -1, -1):
    if i == N - 1:
        continue
    
    if score[i + 1] <= score[i]:
        diff = abs(score[i + 1] - score[i])
        score[i] -= (diff + 1)
        result += (diff + 1)
    
print(result)