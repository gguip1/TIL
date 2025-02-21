string = input()

result = ''

for str in string:
    if ord(str) >= 97:
        result += chr(ord(str) - 32)
    else:
        result += chr(ord(str) + 32)

print(result)
