import sys

N, KIM, LIM = map(int, sys.stdin.readline().rstrip().split())

round = 1

while True:
    if (KIM % 2 == 0) and (LIM == KIM - 1):
        break
    
    if (LIM % 2 == 0) and (KIM == LIM - 1):
        break
    
    if KIM % 2 == 0:
        KIM //= 2
    else:
        KIM //= 2
        KIM += 1

    if LIM % 2 == 0:
        LIM //= 2
    else:
        LIM //= 2
        LIM += 1
    
    round += 1

print(round)

'''
KIM과 LIM이 같은 라운드에서 만날때까지 반복

'''

