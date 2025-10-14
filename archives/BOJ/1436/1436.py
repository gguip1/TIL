import sys

N = int(sys.stdin.readline().rstrip())

def check(num):
    count6 = 0
    
    for n in str(num):
        if n == '6':
            count6 += 1
        else:
            count6 = 0
        
        if count6 == 3:
            return True
    
    return False

num = 666
series = 1
while True:
    if check(num):
        if N == series:
            print(num)
            break
        series += 1
    
    num += 1