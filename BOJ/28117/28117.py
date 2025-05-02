import sys

N = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()
check = [1, 1]

for i in range(2, N):
    check.append(check[i - 2] + check[i - 1])

result = [1]

def mul(list:list):
    mul_value = 1
    for l in list:
        mul_value *= l
    return mul_value

def long_counter(string):
    if len(string) >= 4 and string[:4] == 'long':
        return True
    return False

continues_long = 0
index = 0

while index < N:
    if string[index] == 'l' and long_counter(string[index:]):
        continues_long += 1
        index += 4
    else:
        if continues_long >= 2:
            result.append(check[continues_long])
        continues_long = 0
        index += 1

if continues_long >= 2:
    result.append(check[continues_long])

print(mul(result))
