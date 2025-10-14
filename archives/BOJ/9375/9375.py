import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    clothes = {}
    
    for j in range(n):
        name_, type_ = sys.stdin.readline().rstrip().split()
        
        if clothes.get(type_):
            clothes[type_].append(name_)
        else:
            clothes[type_] = [name_]
    
    lens = []
    for key, value in clothes.items():
        lens.append(len(value) + 1)
    
    result = 1
    for len_ in lens:
        result *= len_
    print(result - 1)
