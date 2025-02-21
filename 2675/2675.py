T = int(input())

result = []

for i in range(T):
    
    R, S = input().split()
    P = ''
    
    for j in range(len(S)):
        P += S[j] * int(R)
    
    result.append(P)

for index, value in enumerate(result):
    print(value)
