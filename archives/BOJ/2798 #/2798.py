N, M = map(int, input().split())

def is_target(num):
    return num <= M

nums = list(map(int, input().split()))

result = 0

# for index, value in enumerate(nums[:-2]):
#     sum_ = value
#     for idx, val in enumerate(nums[index + 1:-1]):
#         sum__ = sum_
#         sum__ += val
#         for i, v in enumerate(nums[index + 2:]):
#             sum___ = sum__
#             sum___ += v
#             if is_target(sum___):
#                 if sum___ > result:
#                     result = sum___

for i in range(N-2):
    for j in range(i + 1, N-1):
        for z in range(j + 1, N):
            if is_target(nums[i] + nums[j] + nums[z]) and nums[i] + nums[j] + nums[z] > result:
                result = nums[i] + nums[j] + nums[z]

print(result)
