import sys
input = sys.stdin.readline

N, M = map(int, input().split())
titles = []

for _ in range(N):
    title, value = input().split()
    titles.append((title, int(value)))

characters = [int(input()) for _ in range(M)]

for character in characters:
    left = 0
    right = N - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if titles[mid][1] < character:
            left = mid + 1
        else:
            right = mid - 1
    
    print(titles[left][0])