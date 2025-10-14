from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))
answer = 0

## 시간 초과
# for a in range(N):
#     for b in range(N - a):
#         if len(set(fruits[a:(N - b)])) <= 2:
#             answer = max(answer, N - (a + b))

a = 0
count = defaultdict(int)
    
for b in range(N):
    count[fruits[b]] += 1
    
    while len(count) > 2:
        count[fruits[a]] -= 1
        if count[fruits[a]] == 0:
            del count[fruits[a]]
        a += 1
    
    answer = max(answer, b - a + 1)
    
print(answer)
