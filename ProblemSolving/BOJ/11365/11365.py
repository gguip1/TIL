pwds = []

while True:
    pwd = input()
    
    if pwd == 'END':
        break
    else:
        pwds.append(pwd)
        
for pwd in pwds:
    for index, value in enumerate(list(pwd)):
        print(list(pwd)[len(pwd) - index - 1], end='')
    print()
