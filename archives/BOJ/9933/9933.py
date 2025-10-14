import sys

N = int(sys.stdin.readline().rstrip())

words = {}

for i in range(N):
    key = sys.stdin.readline().rstrip()
    value = ''.join(reversed(key))
    
    words[key] = value

check = False

for key in words:
    for value in words.values():
        if key == value:
            print(len(key), key[len(key) // 2])
            check = True
        if check:
            break
    if check:
        break