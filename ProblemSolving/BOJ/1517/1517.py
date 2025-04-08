import sys

count = 0

def divide(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    
    return conquer(left, right)

def conquer(left, right):
    global count
    
    conquerList = []
    
    p1 = 0
    p2 = 0
    
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]: # 같은 거는 count X
            conquerList.append(left[p1])
            p1 += 1
        else:
            count += len(left) - p1
            conquerList.append(right[p2])
            p2 += 1

    conquerList.extend(left[p1:])
    conquerList.extend(right[p2:])
    
    return conquerList

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = divide(arr)
print(count)
