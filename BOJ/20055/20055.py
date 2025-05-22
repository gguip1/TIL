import sys


N, K = map(int, sys.stdin.readline().rstrip().split())
conveyor_durability = list(map(int, sys.stdin.readline().rstrip().split()))
robots_position = [False] * N

def check_durability():
    check = 0
    for durability in conveyor_durability:
        if durability == 0:
            check += 1
    return check

step = 0
while check_durability() < K:
    step += 1
    
    conveyor_durability = [conveyor_durability[-1]] + conveyor_durability[:-1]
    robots_position = [robots_position[-1]] + robots_position[:-1]
    robots_position[-1] = False
    
    for i in range(N - 1, -1, -1):
        if robots_position[i] and not robots_position[i + 1] and conveyor_durability[i + 1] >= 1:
            robots_position[i] = False
            robots_position[i + 1] = True
            conveyor_durability[i + 1] -= 1
    
    if not robots_position[0] and conveyor_durability[0] >= 1:
        robots_position[0] = True
        conveyor_durability[0] -= 1
    
    robots_position[-1] = False
    
    # print(f'step #{step} : {conveyor_durability}')
    # print(f'step #{step} : {robots_position}')

print(step)