N, M = map(int, input().split())

result = []

for i in range(N):
    
    bbang = input()
    
    result_ = ""
    
    for j in range(M - 1, -1, -1):
        result_ += bbang[j]
    
    result.append(result_)

for index, value in enumerate(result):
    print(value)