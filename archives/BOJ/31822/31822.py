import sys
input = sys.stdin.readline

c = input()
n = int(input())

answer = 0

for _ in range(n):
    if c[:5] == input()[:5]:
        answer += 1

print(answer)
