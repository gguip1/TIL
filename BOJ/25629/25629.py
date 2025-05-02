N = int(input())
arr = list(map(int, input().split()))

even = 0
odd = 0

for i in range(N):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if N % 2 == 0:
    if even == odd:
        print(1)
    else:
        print(0)
elif N % 2 == 1:
    if even + 1 == odd:
        print(1)
    else:
        print(0)
