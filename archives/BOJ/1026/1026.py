import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0

A.sort(reverse=True)
B.sort()

for index in range(N):
    answer += A[index] * B[index]

print(answer)
