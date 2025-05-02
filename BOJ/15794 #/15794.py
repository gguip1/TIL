import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

min_value = float('inf')
min_count = 0

a.sort()

left = 0
right = n - 1

print(a)

while left < right:
    value = a[left] + a[right]
    diff = abs(v - value)
    
    if diff < min_value:
        min_value = diff
        min_count = 0
    
    if diff == min_value:
        cnt_left = 1
        cnt_right = 1
        while left + cnt_left <= right and a[left + cnt_left] == a[left]:
            cnt_left += 1
        while right + cnt_right >= left and a[right - cnt_right] == a[right]:
            cnt_right += 1
        
        if a[left] == a[right]:
            total = right - left + 1
            min_count += (total * (total - 1)) // 2
            break
        else:
            min_count += cnt_left * cnt_right

        left += cnt_left
        right -= cnt_right
    
    if value < v:
        left += 1
    else:
        right -= 1

# # Brute-Force
# for i in range(n - 1):
#     for j in range(i, n):
#         value = a[i] + a[j]
#         if abs(v - value) < min_value:
#             min_value = abs(v - value)
#             min_count = 1
#         elif abs(v - value) == min_value:
#             min_count += 1

print(min_count)