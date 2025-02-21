T = int(input())

ps_list = [input() for _ in range(T)]

def is_vps(ps):
    
    count = 0
    
    for s in ps:
        if s == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
        
    if count == 0:
        return True
    else:
        return False    


for ps in ps_list:
    if is_vps(ps):
        print('YES')
    else:
        print('NO')
