T = 10

for test in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))
    
    good = 0
    
    for index, building in enumerate(buildings):
        if index - 2 < 0 or index + 2 > len(buildings) - 1:
            continue
        
        check =  min(building - buildings[index - 2],
                    building - buildings[index - 1],
                    building - buildings[index + 1],
                    building - buildings[index + 2])

        if check <= 0:
            good += 0
        else:
            good += check
    
    print(f'#{test} {good}')
