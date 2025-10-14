import sys

N = int(sys.stdin.readline().rstrip())
N_cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
M_cards = list(map(int, sys.stdin.readline().rstrip().split()))

N_cards.sort()
result = []

for m_card in M_cards:
    left = 0
    right = N - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if m_card > N_cards[mid]:
            left = mid + 1
        elif m_card < N_cards[mid]:
            right = mid - 1
        else:
            break
    
    if m_card == N_cards[mid]:
        result.append(1)
    else:
        result.append(0)

print(*result)

# result = {
    
# }

# for m_card in M_cards:
#     result[m_card] = 0

# for n_card in N_cards:
#     if result.get(n_card) == 0:
#         result[n_card] = 1

# print(*result.values())