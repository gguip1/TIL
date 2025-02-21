import sys

def is_palindrome(num):
    if num[:len(num) // 2] == num[:len(num) - (len(num) // 2 + 1):-1]:
        return True
    return False


while True:
    Q = sys.stdin.readline().strip()
    
    if Q == '0':
        break
    
    if is_palindrome(Q):
        print('yes')
    else:
        print('no')
    
