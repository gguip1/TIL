T = int(input())

result = []

for i in range(T):
    
    q = list(input())
    
    score = 0
    
    seq = 1
    
    for index, value in enumerate(q):
        if value == 'O':
            score += seq
            seq += 1
        else:
            seq = 1
    
    result.append(score)

for index, value in enumerate(result):
    print(value)
