import sys
input = sys.stdin.readline

line = input().strip()

minus_nums = []
add_num = 0

num = ''

for l in line:
    if l not in ['-', '+']:
        num += l
    elif l == '-':
        add_num += int(num)
        minus_nums.append(add_num)
        add_num = 0
        num = ''
    elif l == '+':
        add_num += int(num)
        num = ''

add_num += int(num)
minus_nums.append(add_num)

answer = minus_nums[0]

for i in range(1, len(minus_nums)):
    answer -= minus_nums[i]

print(answer)