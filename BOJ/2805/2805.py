import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
trees = list(map(int, input().rstrip().split()))

def sum_trees(value):
    sum_trees_len = 0
    for tree in trees:
        if tree - value > 0:
            sum_trees_len += tree - value
    return sum_trees_len

def binary_search(target_len):
    left = 0
    right = max(trees)
    
    while left <= right:
        mid = (left + right) // 2
        sum_trees_len = sum_trees(mid)
        
        if sum_trees_len < target_len:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

print(binary_search(M))
        