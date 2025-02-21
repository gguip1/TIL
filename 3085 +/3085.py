import sys
import copy

N = int(sys.stdin.readline().strip())

def can_eat_candies(candies):
    max_C = 0
    max_P = 0
    max_Z = 0
    max_Y = 0
    for i in range(N):
        C = 0
        P = 0
        Z = 0
        Y = 0
        previous_C = None
        for j in range(N):
            if previous_C is None:
                previous_C = candies[i][j]
            
            if candies[i][j] == previous_C:
                if candies[i][j] == 'C':
                    C += 1
                elif candies[i][j] == 'P':
                    P += 1
                elif candies[i][j] == 'Z':
                    Z += 1
                elif candies[i][j] == 'Y':
                    Y += 1
            else:
                previous_C = candies[i][j]
                
                if max_C < C:
                    max_C = C
                elif max_P < P:
                    max_P = P
                elif max_Z < Z:
                    max_Z = Z
                elif max_Y < Y:
                    max_Y = Y
                
                if candies[i][j] == 'C':
                    C = 1
                elif candies[i][j] == 'P':
                    P = 1
                elif candies[i][j] == 'Z':
                    Z = 1
                elif candies[i][j] == 'Y':
                    Y = 1
            
        if max_C < C:
            max_C = C
        elif max_P < P:
            max_P = P
        elif max_Z < Z:
            max_Z = Z
        elif max_Y < Y:
            max_Y = Y
    
    for i in range(N):
        C = 0
        P = 0
        Z = 0
        Y = 0
        previous_C = None
        for j in range(N):
            if previous_C is None:
                previous_C = candies[j][i]
            
            if candies[j][i] == previous_C:
                if candies[j][i] == 'C':
                    C += 1
                elif candies[j][i] == 'P':
                    P += 1
                elif candies[j][i] == 'Z':
                    Z += 1
                elif candies[j][i] == 'Y':
                    Y += 1
            else:
                previous_C = candies[j][i]
                
                if max_C < C:
                    max_C = C
                elif max_P < P:
                    max_P = P
                elif max_Z < Z:
                    max_Z = Z
                elif max_Y < Y:
                    max_Y = Y
                
                if candies[j][i] == 'C':
                    C = 1
                elif candies[j][i] == 'P':
                    P = 1
                elif candies[j][i] == 'Z':
                    Z = 1
                elif candies[j][i] == 'Y':
                    Y = 1
            
        if max_C < C:
            max_C = C
        elif max_P < P:
            max_P = P
        elif max_Z < Z:
            max_Z = Z
        elif max_Y < Y:
            max_Y = Y
    
    return max(max_C, max_P, max_Z, max_Y)
            

candies = [list(sys.stdin.readline().strip()) for x in range(N)]

max_candy = 0

for i in range(N):
    for j in range(N - 1):
        temp = candies[i][j]
        candies[i][j] = candies[i][j + 1]
        candies[i][j + 1] = temp
        can_eat_candies_amount = can_eat_candies(candies)
        if max_candy < can_eat_candies_amount:
            max_candy = can_eat_candies_amount
        temp = candies[i][j]
        candies[i][j] = candies[i][j + 1]
        candies[i][j + 1] = temp

for i in range(N):
    for j in range(N - 1):
        temp = candies[j][i]
        candies[j][i] = candies[j + 1][i]
        candies[j + 1][i] = temp
        can_eat_candies_amount = can_eat_candies(candies)
        if max_candy < can_eat_candies_amount:
            max_candy = can_eat_candies_amount
        temp = candies[j][i]
        candies[j][i] = candies[j + 1][i]
        candies[j + 1][i] = temp
            

print(max_candy)
