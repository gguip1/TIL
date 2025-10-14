import sys

S = sys.stdin.readlines()

R_S = ''

result = 0

for s in S:
    R_S += s.replace('\n', '').replace(',',' ')
    
for s in R_S.split():
    result += int(s)
    
print(result)
