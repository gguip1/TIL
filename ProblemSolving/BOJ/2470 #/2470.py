import sys

N = int(sys.stdin.readline().strip())
liquids = list(map(int, sys.stdin.readline().strip().split()))

# def mergeSort(arr, l, r):
#     if l < r:
#         m = int(l + (r - l) / 2)
        
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
        
#         merge(arr, l, m, r)

# def merge(arr, l, m, r):
#     b = [0] * (r - l + 1)
#     i = l
#     j = m + 1
#     k = 0
    
#     while i <= m and j <= r:
#         if arr[i] <= arr[j]:
#             b[k] = arr[i]
#             i += 1
#             k += 1
#         else:
#             b[k] = arr[j]
#             j += 1
#             k += 1
    
#     while i <= m:
#         b[k] = arr[i]
#         i += 1
#         k += 1
    
#     while j <= r:
#         b[k] = arr[j]
#         j += 1
#         k += 1
    
#     while k >= 1:
#         k -= 1
#         arr[l + k] = b[k]

# mergeSort(liquids, 0, N - 1)

liquids.sort()

left = 0
right = N - 1

Q = abs(liquids[left] + liquids[right])
result = [liquids[left], liquids[right]]

while left < right:
    sum = liquids[left] + liquids[right]

    if Q > abs(sum):
        Q = abs(sum)
        result = [liquids[left], liquids[right]]
        if Q == 0:
            break
    
    if sum < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])    

## Case #1: 시간 초과
# diff_0 = None
# min_i = None
# min_j = None

# for i in range(N - 1):
#     for j in range(i + 1, N):
#         if i == j:
#             continue
        
#         diff = abs(liquids[i] + liquids[j])
        
#         if diff_0 is None:
#             diff_0 = diff
#             min_i = i
#             min_j = j
#             continue
        
#         if diff_0 > diff:
#             diff_0 = diff
#             min_i = i
#             min_j = j

# print(liquids[min_i], liquids[min_j])
