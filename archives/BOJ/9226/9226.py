import sys
input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input().strip()

    if word == '#':
        break
    
    for idx in range(len(word)):
        if word[0] in vowels:
            break
        else:
            word = word[1:] + word[0]
    
    print(word + 'ay')
