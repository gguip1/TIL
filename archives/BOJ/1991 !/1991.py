import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def pre_function(root):
    if root != '.':
        print(root, end='')
        pre_function(tree[root][0])
        pre_function(tree[root][1])

def mid_function(root):
    if root != '.':
        mid_function(tree[root][0])
        print(root, end='')
        mid_function(tree[root][1])

def post_function(root):
    if root != '.':
        post_function(tree[root][0])
        post_function(tree[root][1])
        print(root, end='')

pre_function('A')
print()
mid_function('A')
print()
post_function('A')