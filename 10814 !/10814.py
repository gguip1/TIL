import sys

N = int(sys.stdin.readline())

Members = [sys.stdin.readline().strip().split() for x in range(N)]

def quick_sort(members):
    if len(members) <= 1:
        return members
    
    pivot = members[len(members) // 2]
    left = [x for x in members if int(x[0]) < int(pivot[0])]
    middle = [x for x in members if int(x[0]) == int(pivot[0])]
    right = [x for x in members if int(x[0]) > int(pivot[0])]
    
    return quick_sort(left) + middle + quick_sort(right)

# for i in range(N - 1, -1, -1):
#     for j in range(i - 1, -1, -1):
#         if int(Members[i][0]) < int(Members[j][0]):
#             Temp = Members[i]
#             Members[i] = Members[j]
#             Members[j] = Temp

Members = quick_sort(Members)

for member in Members:
    print(member[0], member[1])