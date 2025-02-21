N = int(input())

def lowercase(word):
    result = ''
    for w in word:
        if ord(w) >= ord('a'):
            result += chr(ord(w))
        else:
            result += chr(ord(w) + ord('a') - ord('A'))

    return result

for i in range(N):
    print(lowercase(input()))
