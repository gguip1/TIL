import sys

N = int(sys.stdin.readline().rstrip())
N_cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_cards = list(map(int, sys.stdin.readline().rstrip().split()))

N_cards.sort()

def binary_search(card):
    f_left = 0
    right = N - 1
    
    while f_left <= right:
        mid = (f_left + right) // 2
        
        if N_cards[mid] >= card:
            right = mid - 1
        else:
            f_left = mid + 1
    
    left = 0
    f_right = N - 1
    
    while left <= f_right:
        mid = (left + f_right) // 2
        
        if N_cards[mid] > card:
            f_right = mid - 1
        else:
            left = mid + 1

    return f_right - (f_left - 1)

result = []

for card in M_cards:
    result.append(binary_search(card))

print(*result)