import sys
input = sys.stdin.readline
n = int(input())

def divide(start, end):
    mid = end // 2
    left = divide(start, mid)
    right = divide(mid + 1, end)
    
    return conquer(left, right)

def conquer(left, right):
    