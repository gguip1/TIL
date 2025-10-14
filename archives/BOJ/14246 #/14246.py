import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

# answer = 0

# for x in range(n):
#     for y in range(x + 1, n + 1):
#         if sum(nums[x:y]) > k:
#             answer += 1

# print(answer)

answer = 0
internal_sum = 0
e = 0

for s in range(n):
    while internal_sum <= k and e < n:
        internal_sum += nums[e]
        e += 1
    
    if internal_sum > k:
        answer += n - e + 1
    internal_sum -= nums[s]

print(answer)