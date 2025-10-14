import sys

N, t = map(int, sys.stdin.readline().rstrip().split())

trees = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
trees.sort()

x_1 = trees[0][0]
if x_1 < 0:
    for index, tree in enumerate(trees):
        if index == 0:
            tree[0] = 0
        else:
            tree[0] += abs(x_1)
        
result = [0 for _ in range(N - 1)]

x = 0

for index, tree in enumerate(trees[:-1]):
    
    if tree[0] + tree[1] / t > x:
        x = tree[0] + tree[1] / t
    shadow = (x - trees[index + 1][0]) * t
    
    if shadow > trees[index + 1][1]:
        result[index] = trees[index + 1][1]
    else:
        if result[index] <= shadow:
            x = 0
            result[index] = shadow

print(round(sum(result))) # ? 이게 맞나 부동 소수점 처리를 이렇게 해도됨?
