from collections import deque
import sys


def zigzagSort(arr: list):
    arr.sort()
    
    result = deque()
    
    for index in range(len(arr)):
        if index % 2 == 0:
            result.appendleft(arr.pop())
        else:
            result.append(arr.pop())
    
    return result

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    L = list(map(int, sys.stdin.readline().rstrip().split()))
    
    L = zigzagSort(L)
    
    result = 0
    for index, value in enumerate(L):
        if index == (len(L) - 1):
            if result < abs(value - L[0]):
                result = abs(value - L[0])
        else:
            if result < abs(value - L[index + 1]):
                result = abs(value - L[index + 1])
    
    print(result)