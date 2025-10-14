import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def check(index):
    return A[index] == A[0] + ((index + 1) - 1)

max_sequence = 0
now_sequence = 0

for a_index, a in enumerate(A):
    if check(a_index):
        now_sequence += 1
        max_sequence = max(max_sequence, now_sequence)
    else:
        now_sequence = 0

print(max_sequence)
