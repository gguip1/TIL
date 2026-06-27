def solution(clothes):
    answer = 1
    
    c = {}
    
    for clothe in clothes:
        c[clothe[1]] = c.get(clothe[1], 0) + 1
    
    for value in c.values():
        answer *= value + 1
    
    return answer - 1