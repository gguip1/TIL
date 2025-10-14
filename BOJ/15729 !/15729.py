import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

answer = 0

for i in range(N):
    if nums[i] == 0:
        continue
    answer += 1
    for j in range(3):
        if i + j < N:
            if nums[i + j] == 0:
                nums[i + j] = 1
            else:
                nums[i + j] = 0
    
print(answer)