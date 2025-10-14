import sys
input = sys.stdin.readline

N, K = map(int, input().split())
As = list(map(int, input().split()))

def insertion_sort(As:list):
    for i in range(1, N):
        loc = i - 1
        newItem = As[i]

        print(As)
        while 0 <= loc and newItem < As[loc]:
            As[loc + 1] = As[loc]
            loc -= 1
            print(As)
        
        if loc + 1 != i:
            As[loc + 1] = newItem
        
    return -1

print(insertion_sort(As))