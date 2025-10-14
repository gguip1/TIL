import sys

amount = 1000 - int(sys.stdin.readline().rstrip())
answer = 0
money = [500, 100, 50, 10, 5, 1]

for m in money:
    while amount >= m:
        amount -= m
        answer += 1

print(answer)