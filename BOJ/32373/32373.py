import sys

N, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

result = True

for i in range(N):
    if not i % k == arr[i] % k:
        result = False
        break

if result:
    print('Yes')
else:
    print('No')

## a
# groups = {
    
# }

# for i in range(N):
#     group_index = i % k
#     if groups.get(group_index) is None:
#         groups[group_index] = set()
#     groups[group_index].add(i)

# result = True

# for i in range(N):
#     if not arr[i] in groups[i % k]:
#         result = False
#         break

# if result:
#     print('Yes')
# else:
#     print('No')