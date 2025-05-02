import sys

poem = sys.stdin.readline().rstrip()
space = int(sys.stdin.readline().rstrip())
alphabet = list(map(int, sys.stdin.readline().rstrip().split()))

title = ''
for p in poem.split():
    title += p[0].upper()

previous = None
for current in list(poem):
    if current == previous:
        continue
    
    if current != ' ':
        if current.isupper():
            alphabet[ord(current) - 65] -= 1
        elif current.islower():
            alphabet[ord(current) - 97] -= 1
    else:
        space -= 1
    
    previous = current

for t in title:
    alphabet[ord(t) - 65] -= 1

def check(alphabet):
    for a in alphabet:
        if a < 0:
            return False
    return True

if space >= 0 and check(alphabet):
    print(title)
else:
    print(-1)
