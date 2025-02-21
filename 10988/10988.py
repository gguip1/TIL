import sys

def is_palindrome(word):
    if len(word) % 2 == 1:
        if word[:len(word) // 2] == word[:len(word) // 2:-1]:
            return True
        else:
            return False
    else:
        if word[:len(word) // 2] == word[:len(word) // 2 - 1:-1]:
            return True
        else:
            return False

if is_palindrome(sys.stdin.readline().strip()):
    print(1)
else:
    print(0)
