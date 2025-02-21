import sys

def is_groupWord(word):
    char = []
    prev_char = None
    for c in word:
        if prev_char is None:
            prev_char = c
            char.append(c)
            continue
        
        if prev_char != c and c in char:
            return False
        else:
            prev_char = c
            char.append(c)
        
    return True

N = int(sys.stdin.readline().strip())

words = [sys.stdin.readline().strip() for x in range(N)]

count = 0

for word in words:
    if is_groupWord(word):
        count += 1

print(count)
