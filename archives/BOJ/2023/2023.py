import sys

def check_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

N = int(sys.stdin.readline().rstrip())
result = []
stack = []

for n in range(2, 10):
    if check_prime(n):
        stack.append(n)
        
    while stack:
        num = stack.pop()

        if len(str(num)) == N:
            result.append(num)
            continue
        
        for add_n in range(10):
            next_num = num * 10 + add_n
            if check_prime(next_num):
                stack.append(next_num)

result.sort()
for r in result:
    print(r)