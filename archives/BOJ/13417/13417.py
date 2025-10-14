import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    result = deque()
    
    t = int(sys.stdin.readline().rstrip())
    cards = sys.stdin.readline().rstrip().split()
    
    result.append(cards[0])
    index = 0
    
    for card in cards[1:]:
        if ord(result[index]) < ord(card):
            result.append(card)
        elif index == 0:
            result.appendleft(card)
        else:
            result.appendleft(card)
            index += 1
    
    for r in result:
        print(r, end='')
    print()
