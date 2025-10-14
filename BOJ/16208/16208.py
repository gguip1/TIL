import sys
input = sys.stdin.readline
n = int(input())
iron_sticks = list(map(int, input().split()))
# iron_sticks.sort()

length = sum(iron_sticks)

answer = 0
for iron_stick in iron_sticks:
    answer += iron_stick * (length - iron_stick)
    length -= iron_stick

print(answer)
