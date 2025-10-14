import sys
input = sys.stdin.readline

T = int(input())

def get_dict():
    _dict = {}
    for _ in range(ord('a'), ord('z') + 1):
        _dict[chr(_)] = 0
    return _dict

for _ in range(T):
    encoded_pwd = input().rstrip()
    pwd = input().rstrip()
    
    pwd_list = [0] * 26
    check_list = [0] * 26
    
    for p in pwd:
        pwd_list[ord(p) - 97] += 1

    for e in encoded_pwd[:len(pwd)]:
        check_list[ord(e) - 97] += 1

    if pwd_list == check_list:
        print('YES')
        continue
    
    check = False
    
    for index in range(len(pwd), len(encoded_pwd)):
        check_list[ord(encoded_pwd[index]) - 97] += 1
        check_list[ord(encoded_pwd[index - len(pwd)]) - 97] -= 1
        
        if pwd_list == check_list:
            check = True
            break
    
    if check:
        print('YES')
    else:
        print('NO')