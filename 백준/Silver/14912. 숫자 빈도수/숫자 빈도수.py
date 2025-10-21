import sys
input = sys.stdin.readline

n, d = map(int, input().split())

answer = 0

for i in range(1, n + 1):
    num_s = str(i)
    for num in num_s:
        if num == str(d):
            answer += 1

print(answer)
