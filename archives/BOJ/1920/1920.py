import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
R = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()

def binary_search(num):
    left, right = 0, len(A) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == num:
            return 1
        elif A[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

for r in R:
    print(binary_search(r))
