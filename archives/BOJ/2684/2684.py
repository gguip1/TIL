import sys
input = sys.stdin.readline
P = int(input())
for _ in range(P):
    TTT, TTH, THT, THH, HTT, HTH, HHT, HHH = 0, 0, 0, 0, 0, 0, 0, 0
    _case = input().strip()
    for idx in range(38):
        match _case[idx:idx+3]:
            case 'TTT':
                TTT += 1
            case 'TTH':
                TTH += 1
            case 'THT':
                THT += 1
            case 'THH':
                THH += 1
            case 'HTT':
                HTT += 1
            case 'HTH':
                HTH += 1
            case 'HHT':
                HHT += 1
            case 'HHH':
                HHH += 1
    print(TTT, TTH, THT, THH, HTT, HTH, HHT, HHH)
