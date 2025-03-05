import sys

n = int(sys.stdin.readline().strip())

p1 = [i + 1 for i in range(2 * n)]
p2 = []

for i in range(n):
    card = int(sys.stdin.readline().strip())
    p1.remove(card)
    p2.append(card)

p2.sort()

current_card = -1

while len(p1) > 0 and len(p2) > 0:
    pre_length = len(p2)
    for index, card in enumerate(p2):
        if current_card < card:
            current_card = p2[index]
            p2.pop(index)
            break
    if pre_length == len(p2):
        current_card = -1
    
    if len(p2) == 0:
        break
    
    pre_length = len(p1)
    for index, card in enumerate(p1):
        if current_card < card:
            current_card = p1[index]
            p1.pop(index)
            break
    if pre_length == len(p1):
        current_card = -1
    
    if len(p1) == 0:
        break

print(len(p1))
print(len(p2))
