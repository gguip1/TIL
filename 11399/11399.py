import sys

def min_people(people):
    min_iv = None
    for i, v in enumerate(people):
        if v == -1:
            continue
        
        if min_iv is None:
            min_iv = [i, v]
            continue
        
        if min_iv[1] > v:
            min_iv = [i, v]
    return min_iv

N = int(sys.stdin.readline().strip())

people = list(map(int, sys.stdin.readline().strip().split()))

result = 0
delay = 0

for person in people:
    min_iv = min_people(people)
    result += delay + min_iv[1]
    delay += min_iv[1]
    people[min_iv[0]] = -1

print(result)
