import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

def recursion(elements, depth):
    if depth == M:
        for index, element in enumerate(elements):
            if index != 0:
                print(element, end=' ')
        print()
        return elements
    else:
        for _ in range(elements[-1], N + 1):
            recursion(elements + [_], depth + 1)

recursion([1], 0)