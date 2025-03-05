n = int(input())

sets = []

for i in range(n):
    
    sets.append([int(x) for x in input().split()])

for index, value in enumerate(sets):
    
    Good = True
    
    print('Denominations: ', end='')
    
    for i in range(value[0]):
        
        if i < value[0] - 1:
            if (value[i + 1] * 2 > value[i + 2]):
                Good = False
        
        print(value[i + 1], end=' ')
        
    print()
    
    if Good:
        print('Good coin denominations!')
    else:
        print('Bad coin denominations!')
    
    print()
