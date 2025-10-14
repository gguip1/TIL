result = []

while True:
    o, w = map(int, input().split())
    
    if o == 0 and w == 0:
        break
    
    dead = False
    
    while True:
        act, n = input().split()
        
        if act == '#' and n == '0':
            if dead == True:
                result.append('RIP')
                break
            else:
                if w > o / 2 and w < o * 2:
                    result.append(':-)')
                else:
                    result.append(':-(')
                break
        
        if act == 'E':
            w -= int(n)
        elif act == 'F':
            w += int(n)
            
        if w <= 0:
            dead = True

for index, r in enumerate(result):
    print(index + 1, r)
