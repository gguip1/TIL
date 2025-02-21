N = int(input())
nums = map(int, input().split())
v = int(input())

count = 0

for num in nums:
    if v == num:
        count += 1

print(count)
