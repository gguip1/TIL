import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

prime_nums = set()

def is_prime(num: int):
    if num == 1:
        return False
    for div_num in range(2, int(num ** 0.5) + 1):
        if num % div_num == 0:
            return False
    return True

for num in range(1, 119):
    if is_prime(num):
        prime_nums.add(num)

def is_synthesis(num: int):
    for prime_num in prime_nums:
        if num - prime_num > 0 and num - prime_num in prime_nums:
            return True
    return False

for num in nums:
    if is_synthesis(num):
        print('Yes')
    else:
        print('No')