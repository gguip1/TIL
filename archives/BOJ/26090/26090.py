import sys
input = sys.stdin.readline

def is_prime_num(num):
    if num < 2:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True

def is_perfect_sequence(sequence):
    if is_prime_num(len(sequence)) and is_prime_num(sum(sequence)):
        return True
    return False

N = int(input())
sequence = list(map(int, input().split()))

answer = 0

for start in range(N):
    for end in range(start + 1, N + 1):
        if is_perfect_sequence(sequence[start:end]):
            answer += 1

print(answer)
